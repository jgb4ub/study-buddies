from django.urls import path
from django.contrib import admin
from django.urls import path, include 
from . import views


app_name = 'studyforum'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('post/', views.post, name = 'post'),
    path('groups/', views.groups, name = 'groups'),
    path('postsubmission/',views.postsubmit, name = 'postsubmit'),
    path('groupsubmission/',views.groupsubmit, name = 'groupsubmit'),
    path('<int:id>/addpost/',views.addpost, name='addpost'),
    path('addgroup/',views.addgroup, name = 'addgroup'),
    path('<int:post_id>/postpage/',views.postpage, name='postpage'),
    path('sendchat/', views.messages, name='sendchat'),
    path('sendmessage/',views.sendmessage,name='sendmessage'),
    path('<int:user_id>/<int:group_id>/joingroup/',views.joingroup, name= 'joingroup'),
    path('<str:user_id>/receivechat', views.messageReceived, name='receivechat'),
    path('<int:id>/profile_page/', views.profile_page, name = 'profile_page'),
    path('<int:id>/addcourse/', views.addcourse, name='addcourse'),
    path('coursesubmission/', views.coursesubmit, name='coursesubmit'),
    path('courseremoval/', views.courseremoval, name='courseremoval'),
    path('<int:id>/removecourse/', views.removecourse, name='removecourse'),
    path('courseenrollment/', views.courseenrollment, name='courseenrollment'),
    path('<int:id>/enrollcourse/', views.enrollcourse, name='enrollcourse'),
    path('<int:id>/delete/',views.delete_post,name='delete')
]