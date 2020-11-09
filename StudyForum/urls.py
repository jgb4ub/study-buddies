from django.urls import path
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
    path('<str:username>/profile_page/',views.profile_page, name = 'profile_page'),
    path('<int:id>/profil_epage/', views.profile_page, name = 'profile_page')
]