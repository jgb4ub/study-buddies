from django.db import models
from django.conf import settings
import random
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 12)
    firstname = models.CharField(max_length = 12, default='Sammy')
    lastname = models.CharField(max_length = 12, default = 'Lahrime')
    password = models.CharField(max_length = 12)

class LoginAttempt(models.Model):
    username_passed_in = models.CharField(max_length = 12)
    password_passed_in = models.CharField(max_length = 12)


class Post(models.Model):
    username = models.CharField(max_length = 12, default="na")
    subject = models.CharField(max_length = 50, default="na")
    category = models.CharField(max_length = 20, default="na")
    content = models.CharField(max_length = 100, default="na")
