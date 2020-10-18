from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 12)
    firstname = models.CharField(max_length = 12)
    lastname = models.CharField(max_length = 12)
    password = models.CharField(max_length = 12)

class LoginAttempt(models.Model):
    username_passed_in = models.CharField(max_length = 12)
    password_passed_in = models.CharField(max_length = 12)


class Post(models.Model):
    username = models.CharField(max_length = 12)
    subject = models.CharField(max_length = 50)
    category = models.CharField(max_length = 20)
    content = models.CharField(max_length = 100)