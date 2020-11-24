from django.db import models
from django.conf import settings
from django.utils import timezone
import requests, json
from django.contrib.auth.models import AbstractUser
#from django.contrib.postgres.fields import ArrayField
from twilio.rest import Client
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=12, default="na", unique=True)
    professor = models.CharField(max_length=30, default="na")
    time = models.CharField(max_length=10)

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    year = models.CharField(max_length = 100, default='third year')
    major = models.CharField(max_length = 100, default="computer science")
    phone = models.CharField(max_length = 100, default="")
    email = models.CharField(max_length = 100, default="")
    discord_id = models.CharField(max_length = 100, default="")
    courses = models.ManyToManyField(Course)
    fives = models.ManyToManyField(Course, related_name="fives")
    fours = models.ManyToManyField(Course, related_name="fours")
    threes = models.ManyToManyField(Course, related_name="threes")
    twos = models.ManyToManyField(Course, related_name="twos")
    ones = models.ManyToManyField(Course, related_name="ones")

class LoginAttempt(models.Model):
    username_passed_in = models.CharField(max_length = 12)
    password_passed_in = models.CharField(max_length = 12)

class Post(models.Model):
    username = models.CharField(max_length = 20, default="na")
    subject = models.CharField(max_length = 50, default="na")
    category = models.CharField(max_length = 100, default="na")
    content = models.CharField(max_length = 500, default="na")
    discord_link = models.CharField(max_length = 100, default="na")
    user_id = models.IntegerField(null=True, blank=True)
    

class Group(models.Model):
    group_name = models.CharField(max_length = 100, default="na")
    course = models.CharField(max_length=12, default="na")
    group_description = models.CharField(max_length = 100, default="na")
    creator = models.IntegerField()
    phone = models.CharField(max_length = 12, default="na")
    discord_link = models.CharField(max_length = 100, default="na")

class GroupMember(models.Model):
    first_name = models.CharField(max_length = 12, default="na")
    user_first = models.CharField(max_length = 12, default="na")
    user_last = models.CharField(max_length = 12, default="na")
    group_id = models.IntegerField()
    member_id = models.IntegerField()

class Message(models.Model):
    sender = models.CharField(max_length = 12, default = "anonymous")
    recipient = models.CharField(max_length = 12, default = "anonymous")
    content = models.CharField(max_length = 250, default = "(empty message)")
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#

class Score(models.Model):
    result = models.PositiveIntegerField()
    message = models.CharField(max_length=100, default="na")
    phone = models.CharField(max_length=50, default="na")
    
    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        if self.result < 70:
            #account_sid = 'AC1ea6ae5469fc28d174fcc1961fc5c5a8'
            #auth_token = '923dc7f9846973a05f3b42260672dbc1'
            account_sid = 'ACbdf2883beb2d0ab62072254339ee1624'
            auth_token = '49057a8958e776a081a921354487aed2'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                              body= self.message,
                              #from_='+12285674137',
                              from_='+18559800562',
                              to='+1' + self.phone
                          )

            print(message.sid)
        return super().save(*args, **kwargs)
