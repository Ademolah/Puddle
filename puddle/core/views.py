from django.shortcuts import render

# Create your views here

def index(request):

    return render(request, 'core/index.html')  #second param is the template

def contact(request):
    return render(request, 'core/contact.html')
