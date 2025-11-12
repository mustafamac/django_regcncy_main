from django.shortcuts import render
import requests
def home(request):
    return render(request,'pages/home.html')


def about(request):
    return render(request,'pages/about.html')


def contact(request):
    return render(request,'pages/contact.html')
# Create your views here.

def who_we_are(request):
    #slug = request.GET.get("item")
    #content = WhoWeAreContent.objects.get(slug=slug)
    return render(request, "pages/who_we_are.html")#, {"content": content})