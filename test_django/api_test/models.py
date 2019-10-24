from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=10, verbose_name="用户名")
    user_age = models.CharField(max_length=3, verbose_name="年龄")
    user_position = models.CharField(max_length=10, verbose_name="职位")

    def __str__(self):
        return self.user_name


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=30, verbose_name="项目名称")
    project_version = models.CharField(max_length=10, verbose_name="项目版本")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    create_name = models.ForeignKey("User", on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name
