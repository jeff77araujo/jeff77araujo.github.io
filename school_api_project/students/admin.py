from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Student, Professor, Classroom

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'age', 'link_professor', 'classroom', 'first_semester_grade', 'second_semester_grade')
    list_filter = ('teacher', 'classroom')
    search_fields = ('name', 'teacher__name')
    list_display_links = ('id','name')

    def link_professor(self, obj):
        if obj.teacher:
            url = reverse("admin:students_professor_change", args=[obj.teacher.id])
            return format_html('<a href="{}">{}</a>', url, obj.teacher.name)
        return "-"
    link_professor.short_description = 'Professor'

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    search_fields = ('name', 'email')

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity')
