from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
from django.http import JsonResponse
from .models import Order, Payment, WebhookEvent
import stripe



# Create your views here.
