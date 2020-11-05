from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import LoginAttempt, User, Post, Message

def index(request):
    return render(request, 'studyforum/index.html')

def post(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'studyforum/postings.html',context)

def postsubmit(request):
    return render(request, 'studyforum/posting_submission.html')

def addpost(request):
    new_post_content = request.POST.get("question",False)
    new_post_subject = request.POST.get("submitter", False)
    new_post = Post(content = new_post_content, subject = new_post_subject)
    new_post.save()
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'studyforum/postings.html',context)

def postpage(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'studyforum/postpage.html', {'post': post})

def messages(request, user_id):
    user_messages = Message.objects.filter(recipient=user_id)
    #user_messages2 = Message.objects.filter(recipient=user_id)
    #user_messages = user_messages.union(user_messages2)
    message_list = user_messages.order_by('-time')
    return render(request, 'studyforum/messages.html', {'messages': message_list})
