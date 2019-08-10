from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    # 自定义用户模型
    nickname = models.CharField(max_length=255, default="", verbose_name="昵称")
    job_title = models.CharField(max_length=50, default="", verbose_name="职称")
    introduction = models.TextField(max_length=500, default="", verbose_name="简介")
    avatar = models.FileField(upload_to='avatars/', default="", verbose_name="头像")
    location = models.CharField(max_length=10, default="", verbose_name="位置")
    personal_url = models.URLField(max_length=255, default="", verbose_name="个人主页")
    github = models.URLField(max_length=255, default="", verbose_name="github")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def get_profile_name(self):
        if self.nickname:
            return self.nickname
        return self.username
