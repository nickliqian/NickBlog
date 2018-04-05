from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import six, timezone


class Account(AbstractUser):
    """
    手机号
    个人网站
    所在公司
    工作职位
    所在地
    签名
    """

    sex_choices = (
        (True, '男'),
        (False, '女'),
        (None, '保密'),
    )

    nickname = models.CharField(max_length=50, blank=True)
    gender = models.NullBooleanField(null=True, choices=sex_choices)
    birth = models.DateField(default=timezone.now)

    phone_number = models.CharField(max_length=255, blank=True)
    user_site = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=255, blank=True)
    user_job = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    signature = models.CharField(max_length=255, blank=True)

    class Meta(AbstractUser.Meta):
        pass

