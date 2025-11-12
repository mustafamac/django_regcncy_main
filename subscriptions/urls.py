from django.urls import path
from . import views
app_name = 'subscriptions'
urlpatterns = [
    path('manage/', views.subscribe, name='manage_subscription'), 

]