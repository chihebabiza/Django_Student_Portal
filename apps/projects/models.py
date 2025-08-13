from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web_development', 'Web Development'),
        ('mobile_development', 'Mobile Development'),
        ('data_science', 'Data Science'),
        ('machine_learning', 'Machine Learning'),
        ('cybersecurity', 'Cybersecurity'),
        ('game_development', 'Game Development'),
        ('other', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    requirements = models.TextField(help_text="Required skills and technologies")
    duration = models.CharField(max_length=100, help_text="Expected project duration")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    supervisor = models.CharField(max_length=255, help_text="Project supervisor name")
    max_students = models.IntegerField(default=1, help_text="Maximum number of students")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
