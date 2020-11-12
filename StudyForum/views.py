from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import User, Post, Message, Course

def index(request):
    return render(request, 'studyforum/index.html')

def post(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'studyforum/postings.html',context)

def profile_page(request, id):
    profile = User.objects.get(id=id)
    return render(request, 'studyforum/profile_page.html', {'profile': profile})

def editprofile(request, id):
    return render(request, 'studyforum/index.html')
    
def postsubmit(request):
    return render(request, 'studyforum/posting_submission.html')

def addpost(request):
    new_post_content = request.POST.get("question",False)
    new_post_subject = request.POST.get("submitter", False)
    new_post_course = request.POST.get("course", False)
    new_post_link = request.POST.get("link", False)
    new_post = Post(content = new_post_content, subject = new_post_subject, course = new_post_course, link = new_post_link)
    new_post.save()
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'studyforum/postings.html',context)

def postpage(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'studyforum/postpage.html', {'post': post})

def chat(request):
    return render(request, 'studyforum/chat.html')
#def messages(request, user_id)

def messages(request):
    user_messages = Message.objects.all()
    username_list = User.objects.all()
#    message_list = user_messages.order_by('-time')
    context = {'username_list': username_list}
    return render(request, 'studyforum/sendchat.html', context)

def sendmessage(request):
    message_content = request.POST.get("message",False)
    new_message = Message(content = message_content)
    new_message.save()
    message_list = Message.objects.all()
    context = {'message_list': message_list}
    return render(request, 'studyforum/postings.html',context)

def messageReceived(request, user_id):
    user_messages = Message.objects.filter(recipient=user_id)
    #user_messages2 = Message.objects.filter(recipient=user_id)
    #user_messages = user_messages.union(user_messages2)
    message_list = user_messages.order_by('-time')
    return render(request, 'studyforum/receivechat.html', {'messages': message_list})

def coursesubmit(request):
    return render(request, 'studyforum/course_submission.html')

def addcourse(request, id):
    new_course_name = request.POST.get("name",False)
    new_course_professor = request.POST.get("professor", False)
    new_course = Course(name = new_course_name, professor = new_course_professor)
    new_course.save()
    user = get_object_or_404(User, id=id)
    user.courses.add(new_course)
    user.save
    return render(request, 'studyforum/index.html')

def courseremoval(request):
    return render(request, 'studyforum/course_removal.html')

def removecourse(request, id):
    course_name = request.POST.get("name", False)
    course = get_object_or_404(Course, name=course_name)
    user = get_object_or_404(User, id=id)
    user.courses.remove(course)
    return render(request, 'studyforum/index.html')

def courseenrollment(request):
    return render(request, 'studyforum/course_enrollment.html')

def enrollcourse(request, id):
    course_name = request.POST.get("name", False)
    course = get_object_or_404(Course, name=course_name)
    user = get_object_or_404(User, id=id)
    user.courses.add(course)
    return render(request, 'studyforum/index.html')