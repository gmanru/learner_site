from django.contrib import admin

from .models import Teacher, Course


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = "id", "first_name", "last_name", "full_name"
    list_display_links = "id", "full_name"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    def text_short(self, obj: Course):
        if len(obj.text) > 42:
            return f"{obj.text[:42]}..."
        return obj.text

    list_display = "id", "title", "text_short", "time_to_learn", "ts_created", "ts_last_changed", "teacher"
    list_display_links = "id", "title", "text_short"
