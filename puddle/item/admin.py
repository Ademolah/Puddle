from django.contrib import admin

# Register your models here.
from .models import Category, Item

admin.site.register(Category)     #registering the model to the admin
admin.site.register(Item) #registering the model to the admin)