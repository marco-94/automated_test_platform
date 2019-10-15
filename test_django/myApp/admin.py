from django.contrib import admin
from .models import Grades, Students
# Register your models here.

# 注册


class GradesAdmin(admin.ModelAdmin):
    # 列表页属性
    # 列表显示字段
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum']
    # 列表筛选字段
    list_filter = ['gname']
    # 搜索字段
    search_fields = ['gname']
    # 分页
    list_per_page = 5

    # 添加、修改属性（fields与fieldsets不可同时使用）
    # 字段显示顺序
    # fields = ['gname', 'gboynum', 'gdate', 'ggirlnum']
    # 给分组加属性
    fieldsets = [
        ("num", {"fields": ['ggirlnum', 'gboynum']}),
        ("base", {"fields": ['gname', 'gdate']}),
    ]


admin.site.register(Grades, GradesAdmin)


class StudentsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'sname', 'sage', 'sgender']
    list_per_page = 5


admin.site.register(Students, StudentsAdmin)
