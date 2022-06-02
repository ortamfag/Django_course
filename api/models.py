from django.db import models
from user.models import User


class Student(models.Model):
    user = models.OneToOneField(User, verbose_name='User', on_delete=models.CASCADE)
    projects = models.ManyToManyField("Project", verbose_name='Проекты')
    group = models.ForeignKey("Group", verbose_name='Группа', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Project(models.Model):
    name = models.CharField(verbose_name='Название проекта', max_length=255)
    description = models.TextField(verbose_name='Описание проекта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Group(models.Model):
    number = models.CharField(verbose_name='Номер группы', max_length=50)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
