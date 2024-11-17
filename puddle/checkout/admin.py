from django.contrib import admin
from .models import Order, WebhookEvent, Payment

# Register your models here.
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(WebhookEvent)
