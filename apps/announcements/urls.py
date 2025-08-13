from django.urls import path
from . import views

app_name = 'announcements'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_announcement, name='new'),
]
