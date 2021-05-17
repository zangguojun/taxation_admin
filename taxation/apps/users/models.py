from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(verbose_name='手机号',max_length=11,unique=False)
    class Meta:
        db_table = 'tax_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

