from django.db import models
from django.conf import settings
from django.utils import timezone
import requests, json
from django.contrib.auth.models import AbstractUser
from twilio.rest import Client
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
    course = models.CharField(max_length = 20, default="na")
    link = models.CharField(max_length = 50, default="na")

class Message(models.Model):
    sender = models.CharField(max_length = 12, default = "anonymous")
    recipient = models.CharField(max_length = 12, default = "anonymous")
    content = models.CharField(max_length = 250, default = "(empty message)")
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Score(models.Model):
    result = models.PositiveIntegerField()
    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        if self.result < 70:
            account_sid = 'AC1ea6ae5469fc28d174fcc1961fc5c5a8'
            auth_token = '923dc7f9846973a05f3b42260672dbc1'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                              body='Hi there!',
                              from_='+12285674137',
                              to='+17037178673'
                          )

            print(message.sid)
        return super().save(*args, **kwargs)
