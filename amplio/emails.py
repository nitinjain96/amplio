from validate_email import validate_email

from amplio import models


def is_valid(email_address):
    if validate_email(email_address):
        return True
    else:
        return False


def is_unused(email_address):
    return not models.User.objects.filter(email=email_address).exists()
