from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import User, Post, Message

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
    new_post = Post(content = new_post_content, subject = new_post_subject)
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
    message_sender = request.POST.get("sender", False)
    message_receiver = request.POST.get("receiver",False)
    new_message = Message(content=message_content, sender=message_sender, recipient=message_receiver)
    #new_message.save()

    context = {'messages': new_message}
    return render(request, 'studyforum/receivechat.html',{'messages': new_message})

    #post_list = Post.objects.all()
    #context = {'post_list': post_list}
    #return render(request, 'studyforum/postings.html',context)


def messageReceived(request):
    message_recipient = request.POST.get("receiver",False)
    user_messages = Message.objects.all()
    #user_messages2 = Message.objects.filter(recipient=user_id)
    #user_messages = user_messages.union(user_messages2)
    message_list = user_messages
    #print(message_recipient)
    return render(request, 'studyforum/receivechat.html', {'messages': message_list})
