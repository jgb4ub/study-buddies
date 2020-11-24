from django.test import TestCase
from .models import User, LoginAttempt, Post, Group, GroupMember, Message, Course
# Create your tests here.
class TestCase(TestCase):
    def setUp(self):
        User.objects.create(username="Hero", year="2010", major = "CS")
        Group.objects.create(group_name="study", course="CS3240", group_description="Sam's study", creator="Sam")
        Post.objects.create(username="abcd", subject="hello guys", category="CS", content="need help")
        GroupMember.objects.create(first_name="Davin", group_id=1, member_id=2)
        Message.objects.create(sender="Davin", recipient="Josh", content="hi there")
        Course.objects.create(name="Nate", professor="McBurney", time="12:30-1:15")
        LoginAttempt.objects.create(username_passed_in = "True", password_passed_in = "True")

    def test_user1(self):
        Nick = User.objects.get(major="CS")
        self.assertEqual(Nick.major, "CS")

    def test_user2(self):
        Sam = User.objects.get(major="CS")
        self.assertEqual(Sam.major, "CS")

    def test_user3(self):
        Hero = User.objects.get(major="CS")
        self.assertEqual(Hero.username, "Hero")

    def test_user4(self):
        Hero = User.objects.get(major="CS")
        self.assertNotEqual(Hero.username, "Sam")
        
    def test_user5(self):
        Hero = User.objects.get(username="Hero")
        self.assertEqual(Hero.year, "2010")

    def test_user6(self):
        Hero = User.objects.get(username="Hero")
        self.assertNotEqual(Hero.year, "2015")

    def test_group1(self):
        Davin = Group.objects.get(group_name="study")
        self.assertEqual(Davin.group_name, "study")

    def test_group2(self):
        Davin = Group.objects.get(course="CS3240")
        self.assertNotEqual(Davin.course, "study")

    def test_group3(self):
        Sam = Group.objects.get(creator="Sam")
        self.assertEqual(Sam.creator, "Sam")

    def test_group4(self):
        Sam = Group.objects.get(creator="Sam")
        self.assertNotEqual(Sam.creator, "Davin")

    def test_group5(self):
        Sam = Group.objects.get(creator="Sam")
        self.assertEqual(Sam.group_description, "Sam's study")
    
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

    def test_course1(self):
        course_name = Course.objects.get(name="Nate")
        self.assertEqual(course_name.name, "Nate")

    def test_course2(self):
        course_name = Course.objects.get(name="Nate")
        self.assertNotEqual(course_name.name, "Sam")

    def test_course3(self):
        course_professor = Course.objects.get(name="Nate")
        self.assertEqual(course_professor.professor, "McBurney")

    def test_course4(self):
        course_professor = Course.objects.get(name="Nate")
        self.assertNotEqual(course_professor.professor, "Sam")

    def test_course5(self):
        course_time = Course.objects.get(name="Nate")
        self.assertNotEqual(course_time.time, "10:10-12:00")

    def test_course6(self):
        course_time = Course.objects.get(name="Nate")
        self.assertEqual(course_time.time, "12:30-1:15")

    def test_login1(self):
        attempt = LoginAttempt.objects.get(username_passed_in="True")
        self.assertEqual(attempt.username_passed_in, "True")

    def test_login2(self):
        attempt = LoginAttempt.objects.get(username_passed_in="True")
        self.assertNotEqual(attempt.username_passed_in, "False")

    def test_login3(self):
        attempt = LoginAttempt.objects.get(username_passed_in="True")
        self.assertEqual(attempt.password_passed_in, "True")

    def test_login4(self):
        attempt = LoginAttempt.objects.get(username_passed_in="True")
        self.assertNotEqual(attempt.password_passed_in, "False")
        



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