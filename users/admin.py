from django.contrib import admin

# Register your models here.

from .models import Profile, Skill, Message

admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(Skill)
