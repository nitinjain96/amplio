from django import forms


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
        max_length=255
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'id': 'up-email',
            'placeholder': 'Email address',
        }),
        label='Email address'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'up-password',
            'placeholder': 'Password',
        }),
        label='Password'
    )
