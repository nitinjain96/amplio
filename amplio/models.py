from hashlib import md5

from django.db import models
from django.utils import timezone

from amplio import choices, choice_constants


def user_upload_image(instance, filename):
    email = instance.email
    email_hash = md5(email.encode('utf-8')).hexdigest()
    path = 'amplio/user/{email_hash}'.format(email_hash=email_hash)
    return path


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, primary_key=True)
    password_hash = models.CharField(max_length=2047)
    post = models.IntegerField(choices=choices.USER_POST_CHOICES, default=choice_constants.STUDENT)
    image = models.ImageField(upload_to=user_upload_image, blank=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.IntegerField(choices=choices.FEEDBACK_TYPE_CHOICES, default=choice_constants.NOT_SURE)
    to = models.IntegerField(choices=choices.FEEDBACK_TO_CHOICES, default=choice_constants.IMG)
    category = models.IntegerField(choices=choices.FEEDBACK_CATEGORY_CHOICES,
                                   default=choice_constants.NO_SPECIFIC_CATEGORY)
    image = models.ImageField(upload_to='amplio/feedback/', blank=True)

    time = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)
    status = models.IntegerField(choices=choices.FEEDBACK_STATUS_CHOICES, default=choice_constants.REPORTED)

    by = models.ForeignKey(User, on_delete=models.CASCADE)
    patrons = models.ManyToManyField(User, related_name='patronized_feedback_set')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Feedback, self).save(*args, **kwargs)
        image = self.image
        if image:
            old_name = image.name
            dot_position = old_name.rfind('.')
            new_name = 'amplio/feedback/' + str(self.pk) + old_name[dot_position:]
            if new_name != old_name:
                self.image.storage.delete(new_name)
                self.image.storage.save(new_name, image)
                self.image.name = new_name
                self.image.close()
                self.image.storage.delete(old_name)
        super(Feedback, self).save(*args, **kwargs)


class Comment(models.Model):
    text = models.TextField()

    time = models.DateTimeField(default=timezone.now)
    upon = models.IntegerField(choices=choices.COMMENT_UPON_CHOICES)
    votes = models.IntegerField(default=0)

    upon_feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    upon_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True)
    by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
