from django.urls import path
from . import views

app_name = 'administration'

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('students/', views.students_list, name='students_list'),
    path('student/<int:student_id>/wishlist/', views.student_wishlist_view, name='student_wishlist_view'),
]
