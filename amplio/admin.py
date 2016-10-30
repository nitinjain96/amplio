from django.contrib import admin
from .models import User,Feedback,Comment
# Register your models here.

admin.site.register(User)
admin.site.register(Feedback)
admin.site.register(Comment)
