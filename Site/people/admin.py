from django.contrib import admin

from people.models import *


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Админка пользователя
    """
    list_display = ['get_full_name', 'photo', 'sex', 'status', 'username']
    list_filter = ('status',)
    search_fields = ('get_full_name', 'username')
    save_on_top = True
    fields = ('last_login', 'username', 'password', 'email', 'status', 'first_name', 'last_name',
              'middle_name', 'photo', 'birthday', 'sex', 'is_superuser', 'is_staff',
              'is_active', 'user_permissions', 'groups')

    def get_full_name(self, obj):
        return f'{obj.last_name} {obj.first_name} {obj.middle_name}'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """
    Админка учителя
    """
    list_display = ['get_full_name', 'user', ]

    def get_full_name(self, obj):
        return f'{obj.user.last_name} {obj.user.first_name} {obj.user.middle_name}'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """
    Админка школьника
    """
    list_display = ['get_full_name', 'user', 'class_init']
    list_filter = ('class_init',)

    def get_full_name(self, obj):
        return f'{obj.user.last_name} {obj.user.first_name} {obj.user.middle_name}'


@admin.register(Parents)
class ParentsAdmin(admin.ModelAdmin):
    """
    Админка родителей школьника
    """
    list_display = ['get_full_name', 'user']

    def get_full_name(self, obj):
        return f'{obj.user.last_name} {obj.user.first_name} {obj.user.middle_name}'

