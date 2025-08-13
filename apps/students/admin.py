from django.contrib import admin
from .models import StudentProfile, Wishlist

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_id', 'major', 'year')
    list_filter = ('major', 'year', 'created_at')
    search_fields = ('user__email', 'user__username', 'student_id', 'major')
    ordering = ('-created_at',)

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('student', 'project', 'added_at')
    list_filter = ('added_at', 'project__category')
    search_fields = ('student__email', 'student__username', 'project__title')
    ordering = ('-added_at',)
    readonly_fields = ('added_at',)
