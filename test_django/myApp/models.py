from django.db import models

# Create your models here.

# 创建数据库表


class Grades(models.Model):
    # 班级表
    gname = models.CharField(max_length=20, verbose_name='班级姓名')
    gdate = models.DateTimeField(verbose_name='成立时间')
    ggirlnum = models.IntegerField(verbose_name='女生总数')
    gboynum = models.IntegerField(verbose_name='男生总数')
    idDelete = models.BooleanField(default=False)


class Students(models.Model):
    # 学生表
    sname = models.CharField(max_length=20, verbose_name='学生姓名')
    sgender = models.BooleanField(default=True, verbose_name='学生性别')
    sage = models.IntegerField(verbose_name='学生年龄')
    scontend = models.CharField(max_length=20, verbose_name='学生简介')
    isDelete = models.BooleanField(default=False)
    # 关联外键
    sgrade = models.ForeignKey(Grades, on_delete=models.CASCADE)
