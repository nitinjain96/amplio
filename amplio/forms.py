from hashlib import md5

from django import forms
from django.core.exceptions import ValidationError

from amplio import emails, models, choices


class SignInForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'id': 'in-email',
            'placeholder': 'Email address',
        }),
        label='Email address',
        required=False
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'in-password',
            'placeholder': 'Password',
        }),
        label='Password',
        required=False
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if len(email) == 0:
            raise ValidationError('Please enter your email address', code='missing_email')
        if not emails.is_valid(email):
            raise ValidationError('Please enter a valid email address', code='invalid_email')
        if emails.is_unused(email):
            raise ValidationError('The email address is not associated with any account', code='unused_email')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) == 0:
            raise ValidationError('Please enter your password', code='missing_password')
        return password

    def clean(self):
        email = self.cleaned_data.get('email', '')
        password = self.cleaned_data.get('password', '')
        if email != '' and password != '':
            password_hash = md5(password.encode('utf-8')).hexdigest()
            user = models.User.objects.get(email=email)
            if user.password_hash != password_hash:
                raise ValidationError('Credentials do not match', code='credential_fail')
        return self.cleaned_data


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
            raise ValidationError('Please enter your name', code='missing_name')
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if len(email) == 0:
            raise ValidationError('Please enter your email address', code='missing_email')
        if not emails.is_valid(email):
            raise ValidationError('Please enter a valid email address', code='invalid_email')
        if not emails.is_unused(email):
            raise ValidationError('The email address is already associated with an account', code='used_email')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) == 0:
            raise ValidationError('Please choose a password', code='missing_password')
        if 0 < len(password) < 8:
            raise ValidationError('Your password should be at least 8 characters long', code='short_password')
        return password


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'contact-name',
            'placeholder': 'Name',
        }),
        label='Name',
        max_length=255,
        required=False
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'id': 'contact-email',
            'placeholder': 'Email address',
        }),
        label='Email address',
        required=False
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'id': 'contact-message',
        }),
        label='Message',
        required=False
    )

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) == 0:
            raise ValidationError('Please enter your name', code='missing_name')
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if len(email) == 0:
            raise ValidationError('Please enter your email address', code='missing_email')
        if not emails.is_valid(email):
            raise ValidationError('Please enter a valid email address', code='invalid_email')
        if not emails.is_unused(email):
            raise ValidationError('The email address is already associated with an account', code='used_email')
        return email

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) == 0:
            raise ValidationError('Message cannot be empty', code='missing_message')
        return message


class FeedbackForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'feedback-title',
            'placeholder': 'Title'
        }),
        label='Title',
        required=False
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'id': 'feedback-description'
        }),
        label='Description',
        required=False
    )
    type = forms.ChoiceField(
        widget=forms.Select(attrs={
            'id': 'feedback-type'
        }),
        label='Type',
        choices=choices.FEEDBACK_TYPE_CHOICES,
        required=False
    )
    to = forms.ChoiceField(
        widget=forms.Select(attrs={
            'id': 'feedback-to'
        }),
        label='To',
        choices=choices.FEEDBACK_TO_CHOICES,
        required=False
    )
    category = forms.ChoiceField(
        widget=forms.Select(attrs={
            'id': 'feedback-category'
        }),
        label='Category',
        choices=choices.FEEDBACK_CATEGORY_CHOICES,
        required=False
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'id': 'feedback-image'
        }),
        label='Image',
        required=False
    )

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) == 0:
            raise ValidationError('Please enter a title', code='missing_title')
        return title

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) == 0:
            raise ValidationError('Please enter a description', code='missing_description')
        return description
