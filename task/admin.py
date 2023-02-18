from django.contrib import admin
from .models import Center, Courses, Groups, Students, Marks, Teachers


class CenterAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


class GroupsAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


class StudentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


class MarksAdmin(admin.ModelAdmin):
    list_display = ['student', 'reyting', 'mark', 'created_at']

class TeachersAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']

admin.site.register(Center, CenterAdmin)
admin.site.register(Courses, CenterAdmin)
admin.site.register(Groups, GroupsAdmin)
admin.site.register(Students, StudentsAdmin)
admin.site.register(Marks, MarksAdmin)
admin.site.register(Teachers, TeachersAdmin)
