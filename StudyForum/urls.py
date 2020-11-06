from django.urls import path
from . import views


app_name = 'studyforum'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('post/', views.post, name = 'post'),
    path('postsubmission/',views.postsubmit, name = 'postsubmit'),
    path('addpost/',views.addpost, name='addpost'),
    path('<int:post_id>/postpage/', views.postpage, name='postpage'),
    path('<int:user_id>/profile/', views.profilepage, name = 'profilepage')
]