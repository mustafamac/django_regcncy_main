from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
# Create your views here.
def contact(request):
    return render(request,"contact/contact.html")
