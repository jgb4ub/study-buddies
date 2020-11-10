from django.urls import path
from django.contrib import admin
from django.urls import path, include 
from . import views


app_name = 'studyforum'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('post/', views.post, name = 'post'),
    path('postsubmission/',views.postsubmit, name = 'postsubmit'),
    path('addpost/',views.addpost, name='addpost'),
    path('<int:post_id>/postpage/', views.postpage, name='postpage'),
    path('sendchat/', views.messages, name='sendchat'),
    path('sendmessage/',views.sendmessage,name='sendmessage'),
    path('<str:user_id>/receivechat', views.messageReceived, name='receivechat'),
    path('<int:id>/profile_page/', views.profile_page, name = 'profile_page'),
    path('<int:id>/addcourse/', views.addcourse, name='addcourse'),
    path('coursesubmission/', views.coursesubmit, name='coursesubmit'),
    path('courseremoval/', views.courseremoval, name='courseremoval'),
    path('<int:id>/removecourse/', views.removecourse, name='removecourse'),
    path('courseenrollment/', views.courseenrollment, name='courseenrollment'),
    path('<int:id>/enrollcourse/', views.enrollcourse, name='enrollcourse'),
]