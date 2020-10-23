from django.test import TestCase
from .models import User, LoginAttempt, Post
# Create your tests here.
class TestCase(TestCase):
    def setUp(self):
        User.objects.create(username="di3re", firstname = "Nick", lastname = "Yelp", password = "asdf")
        User.objects.create(username="asdf", firstname = "James", lastname = "David", password = "asdfda")
        Post.objects.create(username = "qe31a",subject = "Math",category = "study",content = "looking for buddy")
        Post.objects.create(username = "ql9cd",subject = "STS",category = "chill",content = "chilling")

    def test_user_firstname(self):
        Nick = User.objects.get(firstname="Nick")
        self.assertEqual(Nick.firstname, "Nick")

    def test_user_lastname(self):
        valid_lastname = User.objects.get(username="asdf")
        self.assertEquals(valid_lastname.lastname, "David")

    def test_user_username(self):
        valid_username = User.objects.get(username="di3re")
        self.assertNotEquals(valid_username.firstname, "Hello")

    def test_user_password(self):
        James = User.objects.get(firstname="James")
        self.assertNotEqual(James.password, "asda")

    def test_login_username(self):
        posting1 = Post.objects.get(username = "qe31a")
        self.assertNotEquals(posting1.username, "di3ree")

    def test_login_subject(self):
        posting2 = Post.objects.get(username = "ql9cd")
        self.assertEquals(posting2.subject, "STS")

    def test_login_category(self):
        posting3 = Post.objects.get(username = "qe31a")
        self.assertEquals(posting3.category, "study")

    def test_login_content(self):
        posting4 = Post.objects.get(username = "ql9cd")
        self.assertEquals(posting4.content, "chilling")
        