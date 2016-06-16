from django.db import models

from amplio import choices


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=2047)
    type = models.CharField(choices=choices.USER_POST_CHOICES)

    def __str__(self):
        return self.name
