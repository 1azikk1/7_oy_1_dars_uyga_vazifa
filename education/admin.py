from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Course, Student


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_photo', 'created_at', 'updated_at')
    list_editable = ('title',)
    actions_on_top = False
    actions_on_bottom = True
    search_fields = ('title',)

    def get_photo(self, course):
        if course.photo:
            return mark_safe(f'<img src="{course.photo.url}" width="200px">')
        else:
            return 'Rasm topilmadi!'

    get_photo.short_description = 'Rasmi'


admin.site.register(Course, CourseAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'course', 'enrolled_at')
    list_editable = ('email', 'course')
    actions_on_top = False
    actions_on_bottom = True
    search_fields = ('name',)
    list_filter = ('enrolled_at',)


admin.site.register(Student, StudentAdmin)
