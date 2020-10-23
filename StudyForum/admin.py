from django.contrib import admin

from .models import LoginAttempt, User, Post


admin.site.register(LoginAttempt)
admin.site.register(User)
admin.site.register(Post)

