from django.http import HttpResponse
from django.shortcuts import render

from amplio import emails
from amplio import forms

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
    return render(request, 'amplio/contact.html')


def search(request):
    return HttpResponse("Work in progress")


def sign_in(request):
    return HttpResponse("Work in progress")


def sign_up(request):
    return HttpResponse("Work in progress")


def terms(request):
    return HttpResponse("Work in progress")
