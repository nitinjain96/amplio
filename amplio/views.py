from hashlib import md5

from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from amplio import models, forms


def index(request):
    sign_in_form = forms.SignInForm()
    sign_up_form = forms.SignUpForm()
    return render(request, 'amplio/index.html', {
        'sign_in_form': sign_in_form,
        'sign_up_form': sign_up_form,
    })


def about(request):
    return render(request, 'amplio/about.html')


def browse(request):
    return HttpResponse("Work in progress")


def compose(request):
    return HttpResponse("Work in progress")


def contact(request):
    if request.method == 'GET':
        form = forms.ContactForm()
        return render(request, 'amplio/contact.html', {
            'state': 'blank',
            'form': form
        })
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            send_content = message + '\n\n' + name + '\n' + email
            thanks = 'Your message has been sent to the developers and designers at IMG. Expect to hear from them soon!'
            send_mail('Contact form submission on Amplio', send_content, 'dhruv_b@live.com', ['dhruv_b@live.com'])
            send_mail('Contact form submission on Amplio', thanks, 'dhruv_b@live.com', [email])
        else:
            return render(request, 'amplio/contact.html', {
                'state': 'failure',
                'form': form,
            })


def profile(request):
    return HttpResponse("Work in progress")


def search(request):
    return HttpResponse("Work in progress")


def sign_in(request):
    if request.method == 'GET':
        form = forms.SignInForm()
        return render(request, 'amplio/sign-in.html', {
            'state': 'blank',
            'form': form,
        })
    if request.method == 'POST':
        form = forms.SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            request.session['user_email'] = email
            return redirect(reverse('amplio:index'))
        else:
            return render(request, 'amplio/sign-in.html', {
                'state': 'failure',
                'form': form,
            })


def sign_up(request):
    if request.method == 'GET':
        form = forms.SignUpForm()
        return render(request, 'amplio/sign-up.html', {
            'state': 'blank',
            'form': form,
        })
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            new_form = forms.SignUpForm()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            password_hash = md5(password.encode('utf-8')).hexdigest()
            user = models.User(name=name, email=email, password_hash=password_hash, post=1)
            user.save()
            return render(request, 'amplio/sign-up.html', {
                'state': 'success',
                'form': new_form,
            })
        else:
            return render(request, 'amplio/sign-up.html', {
                'state': 'failure',
                'form': form,
            })


def sign_out(request):
    request.session.clear()
    request.session.flush()
    return redirect(reverse('amplio:index'))


def terms(request):
    return HttpResponse("Work in progress")
