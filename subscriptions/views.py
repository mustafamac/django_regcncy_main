from django.shortcuts import render
import requests
def subscribe(request):
    return render(request,'subscriptions/subscribe.html')

# Create your views here.
