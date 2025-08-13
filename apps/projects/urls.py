from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    # Public project views
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    
    # Student wishlist views
    path('wishlist/', views.student_wishlist, name='student_wishlist'),
    path('projects/<int:pk>/add-to-wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('projects/<int:pk>/remove-from-wishlist/', views.remove_from_wishlist, name='remove_from_wishlist'),
    
    # Admin project management views
    path('admin/projects/', views.admin_project_list, name='admin_project_list'),
    path('admin/projects/create/', views.create_project, name='create_project'),
    path('admin/projects/<int:pk>/edit/', views.update_project, name='update_project'),
    path('admin/projects/<int:pk>/delete/', views.delete_project, name='delete_project'),
]
