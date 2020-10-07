from django.shortcuts import render

from .models import LoginAttempt, User


def index(request):
    return render(request, 'studyforum/index.html')