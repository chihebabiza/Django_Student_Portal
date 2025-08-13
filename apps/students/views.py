from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wishlist

@login_required
def student_dashboard(request):
    """Student dashboard showing overview of their activities"""
    if request.user.role != 'student':
        messages.error(request, "Access denied. Student privileges required.")
        return redirect('announcements:index')
    
    # Get student's wishlist count
    wishlist_count = Wishlist.objects.filter(student=request.user).count()
    
    # Get recent wishlist items
    recent_wishlist = Wishlist.objects.filter(student=request.user).select_related('project')[:5]
    
    context = {
        'wishlist_count': wishlist_count,
        'recent_wishlist': recent_wishlist,
    }
    return render(request, 'student/dashboard.html', context)
