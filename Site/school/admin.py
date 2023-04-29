from django.contrib import admin

from school.models import *


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    Админка школьных предметов
    """
    list_display = ['name',]


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    """
    Админка классов в школе
    """
    list_display = ['class_num', 'class_index']
