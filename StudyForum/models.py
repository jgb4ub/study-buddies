from django.db import models
from django.conf import settings
from django.utils import timezone
import requests, json
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Course(models.Model):
    rating = models.IntegerField(default=0)
    name = models.CharField(max_length=12, default="na", unique=True)
    professor = models.CharField(max_length=30, default="na")

class User(AbstractUser):
    year = models.CharField(max_length = 100, default='third year')
    major = models.CharField(max_length = 100, default="computer science")
    courses = models.ManyToManyField(Course)

class LoginAttempt(models.Model):
    username_passed_in = models.CharField(max_length = 12)
    password_passed_in = models.CharField(max_length = 12)


class Post(models.Model):
    username = models.CharField(max_length = 12, default="na")
    subject = models.CharField(max_length = 50, default="na")
    category = models.CharField(max_length = 20, default="na")
    content = models.CharField(max_length = 100, default="na")

class Message(models.Model):
    sender = models.CharField(max_length = 12, default = "anonymous")
    recipient = models.CharField(max_length = 12, default = "anonymous")
    content = models.CharField(max_length = 250, default = "(empty message)")
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

