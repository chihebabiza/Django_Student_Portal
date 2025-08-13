from django.db import models

class Announcement(models.Model):
    DISPLAY_CHOICES = [
        ('general', 'General'),
        ('computer_science', 'Computer Science'),
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('math', 'Mathematics'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    display = models.CharField(max_length=50, choices=DISPLAY_CHOICES)
    datetime = models.DateTimeField()

    def __str__(self):
        return self.title
