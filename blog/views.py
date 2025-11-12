

from django.shortcuts import render
import requests
def news_list(request):
    return render(request, 'blog/news_list.html')


def media(request):
    return render(request, 'blog/media.html')


