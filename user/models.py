from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from simple_history.models import HistoricalRecords


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=self.normalize_email(email), password=password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        user.save()
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    date_joined = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Последний вход', auto_now=True)

    is_active = models.BooleanField(verbose_name='Активирован', default=False)
    is_staff = models.BooleanField(default=False, verbose_name='Персонал')
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()
    history = HistoricalRecords()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
