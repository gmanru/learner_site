from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        if request.method != 'GET':
            return Student.objects.filter()
        return Student.objects.filter().prefetch_related("course")

    def display_courses(self, obj: Student):
        courses = obj.course.all()
        return ", ".join((c.name for c in courses))
    
    list_display = "id", "first_name", "last_name", "full_name","age","email","display_courses"
    list_display_links = "id", "full_name"

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = "id", "first_name", "last_name", "full_name"
    list_display_links = "id", "full_name"
