from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import LoginAttempt, User


admin.site.register(LoginAttempt)

admin.site.register(User, UserAdmin)
