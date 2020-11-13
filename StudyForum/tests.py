from django.test import TestCase
from .models import User, LoginAttempt, Post, Group, GroupMember, Message
# Create your tests here.
class TestCase(TestCase):
    def setUp(self):
        User.objects.create(year="2010", major = "CS")
        Group.objects.create(group_name="study", course="CS3240")
        Post.objects.create(username="abcd", subject="hello guys", category="CS", content="need help")
        GroupMember.objects.create(first_name="Davin", group_id=1, member_id=2)
        Message.objects.create(sender="Davin", recipient="Josh",content="hi there")

    def test_year1(self):
        Nick = User.objects.get(major="CS")
        self.assertEqual(Nick.major, "CS")

    def test_year2(self):
        Sam = User.objects.get(major="CS")
        self.assertEqual(Sam.major, "CS")

    def test_group1(self):
        Davin = Group.objects.get(group_name="study")
        self.assertEqual(Davin.group_name, "study")

    def test_group2(self):
        Davin = Group.objects.get(course="CS3240")
        self.assertNotEqual(Davin.course, "study")
    
    def test_post1(self):
        You = Post.objects.get(username="abcd")
        self.assertEqual(You.username, "abcd")

    def test_post2(self):
        You = Post.objects.get(username="abcd")
        self.assertEqual(You.subject, "hello guys")
    
    def test_post3(self):
        You = Post.objects.get(username="abcd")
        self.assertNotEqual(You.category, "abcd")
    
    def test_post4(self):
        You = Post.objects.get(username="abcd")
        self.assertEqual(You.content, "need help")

    def test_groupmember1(self):
        You = GroupMember.objects.get(first_name="Davin")
        self.assertEqual(You.first_name, "Davin")

    def test_groupmember2(self):
        You = GroupMember.objects.get(first_name="Davin")
        self.assertEqual(You.group_id,1)

    def test_groupmember3(self):
        You = GroupMember.objects.get(first_name="Davin")
        self.assertEqual(You.member_id, 2)

    def test_message1(self):
        h = Message.objects.get(sender="Davin")
        self.assertNotEqual(h.sender, "Sammy")
    
    def test_message2(self):
        h = Message.objects.get(sender="Davin")
        self.assertEqual(h.sender, "Davin")

    def test_message3(self):
        h = Message.objects.get(sender="Davin")
        self.assertEqual(h.recipient, "Josh")

    def test_message4(self):
        h = Message.objects.get(sender="Davin")
        self.assertEqual(h.content, "hi there")
    



    '''
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
        '''
