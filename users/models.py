from django.db import models
from django.contrib.auth.models import AbstractUser


null_options = {'blank': True, 'null': True}

# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, verbose_name='phone', **null_options)
    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', **null_options)
    country = models.CharField(max_length=100, verbose_name='country', **null_options)

    token = models.CharField(max_length=100, verbose_name='token', **null_options)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

