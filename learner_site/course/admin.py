from django.contrib import admin
from .models import City, Course, StudentInCources

admin.site.register(City)
admin.site.register(Course)

@admin.register(StudentInCources)
class StudentInCourcesAdmin(admin.ModelAdmin):
    list_display = "id", "course", "student"
    list_display_links = "id", "course", "student",
