from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager,\
    PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):
        """ Creates and saves a new user """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """ Creates and saves a new super user"""
        user = self.create_user(username, password)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    is_student = models.BooleanField(blank=True)
    is_teacher = models.BooleanField(blank=True)
    objects = UserManager()

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
