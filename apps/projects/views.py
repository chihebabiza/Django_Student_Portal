from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Project
from .forms import ProjectForm
from apps.students.models import Wishlist

@login_required
def project_list(request):
    """Display all projects with filtering options - Student access only"""
    if request.user.role != 'student':
        messages.error(request, "Access denied. Student privileges required to view projects.")
        return redirect('announcements:index')
    
    projects = Project.objects.filter(status='available')
    category_filter = request.GET.get('category')
    search_query = request.GET.get('search')
    
    if category_filter:
        projects = projects.filter(category=category_filter)
    
    if search_query:
        projects = projects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(requirements__icontains=search_query)
        )
    
    # Get user's wishlist
    user_wishlist = list(Wishlist.objects.filter(student=request.user).values_list('project_id', flat=True))
    
    context = {
        'projects': projects,
        'category_filter': category_filter,
        'search_query': search_query,
        'user_wishlist': user_wishlist,
        'categories': Project.CATEGORY_CHOICES,
    }
    return render(request, 'projects/project_list.html', context)

@login_required
def project_detail(request, pk):
    """Display detailed view of a project - Student access only"""
    if request.user.role != 'student':
        messages.error(request, "Access denied. Student privileges required to view project details.")
        return redirect('announcements:index')
    
    project = get_object_or_404(Project, pk=pk)
    is_wishlisted = Wishlist.objects.filter(student=request.user, project=project).exists()
    
    context = {
        'project': project,
        'is_wishlisted': is_wishlisted,
    }
    return render(request, 'projects/project_detail.html', context)

@login_required
def add_to_wishlist(request, pk):
    """Add a project to student's wishlist"""
    if request.user.role != 'student':
        messages.error(request, "Only students can add projects to wishlist.")
        return redirect('projects:project_detail', pk=pk)
    
    project = get_object_or_404(Project, pk=pk)
    wishlist_item, created = Wishlist.objects.get_or_create(
        student=request.user,
        project=project
    )
    
    if created:
        messages.success(request, f"'{project.title}' has been added to your wishlist.")
    else:
        messages.info(request, f"'{project.title}' is already in your wishlist.")
    
    return redirect('projects:project_detail', pk=pk)

@login_required
def remove_from_wishlist(request, pk):
    """Remove a project from student's wishlist"""
    if request.user.role != 'student':
        messages.error(request, "Only students can manage wishlist.")
        return redirect('projects:project_detail', pk=pk)
    
    project = get_object_or_404(Project, pk=pk)
    try:
        wishlist_item = Wishlist.objects.get(student=request.user, project=project)
        wishlist_item.delete()
        messages.success(request, f"'{project.title}' has been removed from your wishlist.")
    except Wishlist.DoesNotExist:
        messages.error(request, "Project not found in your wishlist.")
    
    return redirect('projects:project_detail', pk=pk)

@login_required
def student_wishlist(request):
    """Display student's wishlist"""
    if request.user.role != 'student':
        messages.error(request, "Only students can view wishlist.")
        return redirect('projects:project_list')
    
    wishlist_items = Wishlist.objects.filter(student=request.user).select_related('project')
    
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, 'projects/student_wishlist.html', context)

# Admin views for CRUD operations
@login_required
def admin_project_list(request):
    """Admin view to manage all projects"""
    if request.user.role != 'admin':
        messages.error(request, "Access denied. Admin privileges required.")
        return redirect('projects:project_list')
    
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'admin/admin_project_list.html', context)

@login_required
def create_project(request):
    """Admin view to create new project"""
    if request.user.role != 'admin':
        messages.error(request, "Access denied. Admin privileges required.")
        return redirect('projects:project_list')
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Project created successfully.")
            return redirect('projects:admin_project_list')
    else:
        form = ProjectForm()
    
    context = {'form': form, 'action': 'Create'}
    return render(request, 'admin/project_form.html', context)

@login_required
def update_project(request, pk):
    """Admin view to update existing project"""
    if request.user.role != 'admin':
        messages.error(request, "Access denied. Admin privileges required.")
        return redirect('projects:project_list')
    
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project updated successfully.")
            return redirect('projects:admin_project_list')
    else:
        form = ProjectForm(instance=project)
    
    context = {'form': form, 'project': project, 'action': 'Update'}
    return render(request, 'admin/project_form.html', context)

@login_required
def delete_project(request, pk):
    """Admin view to delete project"""
    if request.user.role != 'admin':
        messages.error(request, "Access denied. Admin privileges required.")
        return redirect('projects:project_list')
    
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        project.delete()
        messages.success(request, f"Project '{project.title}' has been deleted.")
        return redirect('projects:admin_project_list')
    
    context = {'project': project}
    return render(request, 'admin/project_confirm_delete.html', context)
