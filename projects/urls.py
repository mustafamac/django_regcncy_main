from django.urls import path
from . import views
app_name = 'projects'
urlpatterns = [
    path('project_detail/', views.detail, name='project_detail'),
    path('project_list/', views.list, name='project_list'),

]