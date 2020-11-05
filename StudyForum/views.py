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

def messageReceived(request):
    message_list = Message.objects.all()
    context = {'message_list': message_list}
    return render(request, 'studyforum/receivechat.html',context)
