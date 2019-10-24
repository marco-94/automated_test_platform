from django.contrib import admin
from .models import User, Project

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_age', 'user_position']
    search_fields = ['user_name', 'user_age', 'user_position']
    list_filter = ['user_name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'project_version', 'create_time', 'create_name']
    search_fields = ['project_name', 'project_version', 'create_time', 'create_name']
    list_filter = ['project_name']
