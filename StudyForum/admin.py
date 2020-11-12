from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Course
from .models import LoginAttempt, User, Score

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Account information", {'fields': ['courses']})
    ]

admin.site.register(LoginAttempt)
admin.site.register(Course)
admin.site.register(User, UserAdmin)
admin.site.register(Score)
