from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import LoginAttempt, User, Forum, Post


def index(request):
    return render(request, 'studyforum/index.html')

def post(request):
    post_list = Post.objects.all()
	context = {'post_list':post_list}
	return render(request, 'studyforum/postings/html',context)