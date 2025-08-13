from django.shortcuts import render, get_object_or_404, redirect
from .models import Announcement
from .forms import AnnouncementForm

# CREATE
def new_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('announcements:index')
    else:
        form = AnnouncementForm()
    return render(request, 'announcements/create.html', {'form': form})

# READ (List)
def index(request):
    filter_param = request.GET.get('filter')
    announcements = Announcement.objects.all().order_by('-datetime')
    
    if filter_param:
        announcements = announcements.filter(display=filter_param)
    
    context = {
        'announcements': announcements,
        'filter': filter_param,
    }
    return render(request, 'index.html', context)

# UPDATE
def update_announcement(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('announcement_list')
    else:
        form = AnnouncementForm(instance=announcement)
    return render(request, 'announcements/update.html', {'form': form})

# DELETE
def delete_announcement(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        announcement.delete()
        return redirect('announcement_list')
    return render(request, 'announcements/delete.html', {'announcement': announcement})
