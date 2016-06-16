from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'amplio/index.html')


def search(request):
    return HttpResponse("Work in progress")


def sign_up(request):
    return HttpResponse("Work in progress")


def log_in(request):
    return HttpResponse("Work in progress")


def compose(request):
    return HttpResponse("Work in progress")
