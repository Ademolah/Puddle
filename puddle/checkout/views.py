from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
from django.http import JsonResponse
from .models import Order, Payment, WebhookEvent
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    if request.method == 'POST':
        #get product details from the request
        product_name = request.POST.get('product_name')
        quantity = int(request.POST.get('quantity'))
        total_amount = float(request.POST.get('total_amount'))

        #create an order
        order = Order.objects.create(
            user = request.user,
            product_name = product_name,
            quantity = quantity,
            total_amount =total_amount,
            order_status = 'Pending'
        )

        #stripe checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items =[
                {
                    'price_data':{
                        'currency':'NGN',
                        'product_data':{
                            'name':product_name
                        },
                        'unit_amount':int(total_amount*100)  #amount has to be in cents
                    },
                    'quantity': quantity
                },
            ],
            mode='payment',
            success_url=request.build_absolute_uri('/success/')+'?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri('/cancel/')
        )

        #Save the payment information
        Payment.objects.create(
            order=order,
            amount = total_amount,
            stripe_payment_id = checkout_session.id,
            payment_status = 'Pending'
        )

        #redirect to the stripe checkout page
        return JsonResponse({'id': checkout_session.id})
    
    #Render a checkout page for get request
    return render(request, 'checkout/checkout.html')


