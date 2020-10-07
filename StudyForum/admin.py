from django.contrib import admin

from .models import LoginAttempt, User


admin.site.register(LoginAttempt)
admin.site.register(User)


