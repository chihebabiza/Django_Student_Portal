from django.db import models
from django.conf import settings
from apps.projects.models import Project

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    major = models.CharField(max_length=100)
    year = models.IntegerField(help_text="Academic year (1-4)")
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True, help_text="Brief description about yourself")
    skills = models.TextField(blank=True, help_text="Your technical skills")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.student_id}"

class Wishlist(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wishlist')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='wishlisted_by')
    added_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, help_text="Optional notes about why you're interested")

    class Meta:
        unique_together = ('student', 'project')
        ordering = ['-added_at']

    def __str__(self):
        return f"{self.student.username} - {self.project.title}"
