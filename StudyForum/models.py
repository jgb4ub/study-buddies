from django.db import models
from django.conf import settings
from django.utils import timezone
import requests, json
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    description = models.CharField(max_length = 100, default='Sammy')
    somethingplease = models.CharField(max_length = 100, default="please work")

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
    def __str__(self):
        return (self.content+self.recipient)
