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

def postrender(request, post_id):
    post = Post.objects.get(pk=post_id)
    selected = post.choice_set.get(pk=request.POST['choice'])
    

def addpost(request):
    new_post_content = request.POST.get("submitter",False)
    new_post = Post(content = new_post_content)
    new_post.subject = "testing the post"
    new_post.save()
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'studyforum/postings.html',context)
