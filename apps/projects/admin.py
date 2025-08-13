from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'supervisor', 'max_students', 'created_at')
    list_filter = ('category', 'status', 'created_at')
    search_fields = ('title', 'description', 'supervisor')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'category', 'status')
        }),
        ('Project Details', {
            'fields': ('requirements', 'duration', 'supervisor', 'max_students')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
