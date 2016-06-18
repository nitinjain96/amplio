from django import forms


class SignUpForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'up-name',
        }),
        label='Name',
        max_length=255
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'id': 'up-email',
        }),
        label='Email address'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'up-password',
        }),
        label='Password'
    )

