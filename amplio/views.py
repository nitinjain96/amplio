from hashlib import md5

from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponse, Http404
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
    feedback_list = None
    if request.method == 'GET':
        sort_by = '-votes'
        feedback_list = models.Feedback.objects.order_by(sort_by)[:20]
    if request.method == 'POST':
        sort_by = request.POST.get('sort_by')
        start = request.POST.get('start')
        end = request.POST.get('end')
        feedback_list = models.Feedback.objects.order_by(sort_by)[start:end]
    return render(request, 'amplio/browse.html', {'feedback_list': feedback_list})


def compose(request):
    user_email = request.session.get('user_email', '')
    if len(user_email) == 0:
        return redirect(reverse('amplio:sign_in'))
    if request.method == 'GET':
        form = forms.FeedbackForm()
        return render(request, 'amplio/compose.html', {
            'state': 'blank',
            'form': form
        })
    if request.method == 'POST':
        form = forms.FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = forms.FeedbackForm()
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            type = form.cleaned_data.get('type')
            to = form.cleaned_data.get('to')
            category = form.cleaned_data.get('category')
            image = form.cleaned_data.get('image')
            user = models.User.objects.get(email=user_email)
            feedback = models.Feedback(
                title=title,
                description=description,
                type=type, to=to,
                category=category,
                image=image,
                by=user
            )
            feedback.save()
            return render(request, 'amplio/compose.html', {
                'state': 'success',
                'form': new_form,
            })
        else:
            return render(request, 'amplio/compose.html', {
                'state': 'failure',
                'form': form,
            })


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
    email = request.session.get('user_email', '')
    if len(email) == 0:
        return redirect(reverse('amplio:sign_in'))
    user = models.User.objects.get(email=email)
    return render(request, 'amplio/profile.html', {'user': user})


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
            user = models.User.objects.get(email=email)
            request.session['user_name'] = user.name
            request.session['user_email'] = user.email
            request.session['user_name_email_hash'] = md5((user.name+user.email).encode('utf-8')).hexdigest()
            if user.image:
                request.session['user_image_url'] = user.image.url
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
    return render(request, 'amplio/terms.html')


def vote(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        feedback = models.Feedback.objects.get(pk=id)
        feedback.votes += 1
        feedback.save()
        return HttpResponse(feedback.votes)
    else:
        raise Http404('No GET interface has been defined for amplio.views.vote')
