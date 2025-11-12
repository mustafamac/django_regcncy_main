from django.shortcuts import render
import requests
# Create your views here.
def detail(request):
    return render(request,"projects/project_detail.html")

def list(request):
    return render(request,"projects/project_list.html")


