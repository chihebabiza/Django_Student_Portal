from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from apps.announcements.models import Announcement
from apps.projects.models import Project
from apps.students.models import Wishlist, StudentProfile
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def admin_dashboard(request):
    """Admin dashboard showing overview of the system"""
    if request.user.role != 'admin':
        messages.error(request, "Access denied. Admin privileges required.")
        return redirect('announcements:index')
    
    # Get statistics
    total_announcements = Announcement.objects.count()
    total_projects = Project.objects.count()
    total_students = User.objects.filter(role='student').count()
    total_wishlists = Wishlist.objects.count()
    
    # Get recent activities
    recent_announcements = Announcement.objects.order_by('-datetime')[:5]
    recent_projects = Project.objects.order_by('-created_at')[:5]
    
    # Get popular projects (most wishlisted)
    popular_projects = Project.objects.annotate(
        wishlist_count=Count('wishlisted_by')
    ).order_by('-wishlist_count')[:5]
    
    context = {
        'total_announcements': total_announcements,
        'total_projects': total_projects,
        'total_students': total_students,
        'total_wishlists': total_wishlists,
        'recent_announcements': recent_announcements,
        'recent_projects': recent_projects,
        'popular_projects': popular_projects,
    }
    return render(request, 'admin/dashboard.html', context)

@login_required
def student_wishlist_view(request, student_id):
    """Admin view to see a specific student's wishlist"""
    if request.user.role != 'admin':
        messages.error(request, "Access denied. Admin privileges required.")
        return redirect('announcements:index')
    
    student = get_object_or_404(User, id=student_id, role='student')
    wishlist_items = Wishlist.objects.filter(student=student).select_related('project')
    
    context = {
        'student': student,
        'wishlist_items': wishlist_items,
    }
    return render(request, 'admin/student_wishlist.html', context)

@login_required
def students_list(request):
    """Admin view to see all students and their wishlists"""
    if request.user.role != 'admin':
        messages.error(request, "Access denied. Admin privileges required.")
        return redirect('announcements:index')
    
    students = User.objects.filter(role='student').annotate(
        wishlist_count=Count('wishlist')
    ).order_by('username')
    
    context = {
        'students': students,
    }
    return render(request, 'admin/students_list.html', context)
