from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import LoginAttempt, User, Post

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

def profilepage(request, id):
    found = False
    profileList = User.objects.all()
    for i in profileList:
        if i.userid == id:
            profile = i
            found = True
    if not found:
        profile = User(userid=id)
    return render(request, 'studyforum/profilepage.html', {'profile': profile})
