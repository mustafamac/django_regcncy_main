
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # صفحة قائمة الأخبار
    path('news_list/', views.news_list, name='news_list'),
    path('media/', views.media, name='media'),
    
   
]

