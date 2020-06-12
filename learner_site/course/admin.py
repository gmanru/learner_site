from django.contrib import admin
from .models import City, Course, StudentInCources

admin.site.register(City)
#admin.site.register(Course)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = "id","name", "students","teachers"
    list_display_links = "id",

@admin.register(StudentInCources)
class StudentInCourcesAdmin(admin.ModelAdmin):
    list_display = "id","student","course"
    list_display_links = "id",
