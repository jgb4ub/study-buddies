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
    username = models.CharField(max_length = 12)
    subject = models.CharField(max_length = 50)
    category = models.CharField(max_length = 20)
    content = models.CharField(max_length = 100)
<<<<<<< HEAD

class PostRender(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


=======
    postID = models.CharField(max_length=100, default=models.ForeignKey("self", on_delete=models.CASCADE))
>>>>>>> f3cc0e993d93ceb70ca6fd2cf6b70ae7f04293ff
