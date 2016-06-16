from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.db import models

from amplio import choices
from django_apps import settings

fs = FileSystemStorage(location=settings.STATIC_URL)


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=2047)
    post = models.IntegerField(choices=choices.USER_POST_CHOICES)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.IntegerField(choices=choices.FEEDBACK_TYPE_CHOICES)
    to = models.IntegerField(choices=choices.FEEDBACK_TO_CHOICES)
    category = models.IntegerField(choices=choices.FEEDBACK_CATEGORY_CHOICES)
    image = models.ImageField(upload_to='amplio/images', storage=fs, blank=True)

    time = models.DateTimeField(default=datetime.now)
    votes = models.IntegerField(default=0)

    by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()

    time = models.DateTimeField(default=datetime.now)
    upon = models.IntegerField(choices=choices.COMMENT_UPON_CHOICES)
    votes = models.IntegerField(default=0)

    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True)
    by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
