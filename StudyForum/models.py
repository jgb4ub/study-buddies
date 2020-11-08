from django.db import models 
from django.conf import settings
import random
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 12, default="default name")
    firstname = models.CharField(max_length = 12, default='Sammy')
    lastname = models.CharField(max_length = 12, default = 'Lahrime')
    userid = models.CharField(max_length=10, default="0")

class courses(models.Model):
    className = models.CharField(max_length = 20)
    classNumber = models.CharField(max_length=10)

class LoginAttempt(models.Model):
    username_passed_in = models.CharField(max_length = 12)
    password_passed_in = models.CharField(max_length = 12)


class Post(models.Model):
    username = models.CharField(max_length = 12)
    subject = models.CharField(max_length = 50)
    category = models.CharField(max_length = 20)
    content = models.CharField(max_length = 100)