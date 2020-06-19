from django.contrib import admin
from .models import City, Course, StudentInCources

admin.site.register(City)
#admin.site.register(Course)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        if request.method != 'GET':
            return Course.objects.filter()
        return Course.objects.filter().prefetch_related("students")

    def display_students(self, obj: Course):
        students = obj.students.all()
        return ", ".join((s.first_name for s in students))
    list_display = "id","name", "display_students","teachers"
    list_display_links = "id",

@admin.register(StudentInCources)
class StudentInCourcesAdmin(admin.ModelAdmin):
    list_display = "id","student","course"
    list_display_links = "id",
