from django import forms
from django.core.exceptions import ValidationError

from amplio import emails


class SignInForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'id': 'in-email',
            'placeholder': 'Email address',
        }),
        label='Email address'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'in-password',
            'placeholder': 'Password',
        }),
        label='Password'
    )


class SignUpForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'up-name',
            'placeholder': 'Name',
        }),
        label='Name',
        max_length=255,
        required=False
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'id': 'up-email',
            'placeholder': 'Email address',
        }),
        label='Email address',
        required=False
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'up-password',
            'placeholder': 'Password',
        }),
        label='Password',
        required=False
    )

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) == 0:
            raise ValidationError("Please enter your name", code='missing_name')
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if len(email) == 0:
            raise ValidationError("Please enter your email address", code='missing_email')
        if not emails.is_valid(email):
            raise ValidationError("Please enter a valid email address", code='invalid_email')
        if not emails.is_unused(email):
            raise ValidationError("The email address is already associated with an account", code='used_email')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) == 0:
            raise ValidationError("Please choose a password")
        if 0 < len(password) < 8:
            raise ValidationError("Your password should be at least 8 characters long")
        return password
