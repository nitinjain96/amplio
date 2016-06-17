from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'amplio/index.html')


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
