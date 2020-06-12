from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = "id", "first_name", "last_name", "full_name","age","email"
    list_display_links = "id", "full_name"

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = "id", "first_name", "last_name", "full_name"
    list_display_links = "id", "full_name"
