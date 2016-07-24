from hashlib import md5

from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from amplio import models, forms, choice_constants


def populate_session(request, user):
    request.session['user_name'] = user.name
    request.session['user_email'] = user.email
    request.session['user_name_email_hash'] = user.name_email_hash
    if user.image:
        request.session['user_image_url'] = user.image.url
    else:
        if 'user_image_url' in request.session:
            del request.session['user_image_url']


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
        feedback_list = models.Feedback.objects.annotate(patron_count=Count('patrons')).order_by('-patron_count')[:20]
    email = request.session.get('user_email', '')
    if len(email) == 0:
        user = None
    else:
        user = models.User.objects.get(email=email)
    return render(request, 'amplio/browse.html', {'feedback_list': feedback_list, 'user': user})


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
            feedback_type = form.cleaned_data.get('type')  # Just so that the inbuilt 'type' is not overshadowed
            to = form.cleaned_data.get('to')
            category = form.cleaned_data.get('category')
            image = form.cleaned_data.get('image')
            user = models.User.objects.get(email=user_email)
            feedback = models.Feedback(
                title=title,
                description=description,
                type=feedback_type, to=to,
                category=category,
                author=user
            )
            feedback.save()
            # Now object has an ID which will be used in setting the save path for the image
            feedback.image = image
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


def delete_account(request):
    email = request.session.get('user_email', '')
    if len(email) == 0:
        return redirect(reverse('amplio:sign_in'))
    request.session.clear()
    request.session.flush()
    user = models.User.objects.get(email=email)
    user.delete()
    return redirect(reverse('amplio:index'))


def detail(request, feedback_id):
    if request.method == 'GET':
        try:
            email = request.session.get('user_email', '')
            if len(email) == 0:
                user = None
            else:
                user = models.User.objects.get(email=email)
            feedback = models.Feedback.objects.get(pk=feedback_id)
            tier_one = feedback.comment_set.filter(upon_comment=None)
            return render(request, 'amplio/detail.html', {
                'tier_one': tier_one,
                'user': user,
                'feedback': feedback,
            })
        except models.Feedback.DoesNotExist:
            raise Http404('This feedback item does not exist')


def profile(request):
    email = request.session.get('user_email', '')
    if len(email) == 0:
        return redirect(reverse('amplio:sign_in'))
    user = models.User.objects.get(email=email)
    if request.method == 'GET':
        data = {
            'name': user.name,
            'image': user.image,
        }
        form = forms.EditProfileForm(data=data)
        return render(request, 'amplio/profile.html', {
            'user': user,
            'state': 'blank',
            'form': form,
        })
    if request.method == 'POST':
        form = forms.EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name', '')
            image = form.cleaned_data.get('image')
            user.name = name
            if image is not None:
                user.image = image
            user.save()
            populate_session(request, user)
            return render(request, 'amplio/profile.html', {
                'user': user,
                'state': 'success',
                'form': form,
            })
        else:
            return render(request, 'amplio/profile.html', {
                'user': user,
                'state': 'failure',
                'form': form,
            })


def remove_image(request):
    if request.method == 'POST':
        email = request.session.get('user_email', '')
        if len(email) == 0:
            raise Http404('You need to be logged in to access this interface')
        user = models.User.objects.get(email=email)
        user.image = None
        user.save()
        populate_session(request, user)
        return HttpResponse('OK')
    else:
        raise Http404('No GET interface has been defined for amplio.views.remove_image')


def reply(request):
    if request.method == 'POST':
        email = request.session.get('user_email', '')
        if len(email) == 0:
            raise Http404('You need to be logged in to access this interface')
        user = models.User.objects.get(email=email)

        comment_id = request.POST.get('upon_comment', '')
        if comment_id == '':
            return HttpResponse('Improper input upon_comment')

        feedback_id = request.POST.get('upon_feedback', '')
        if comment_id == '':
            return HttpResponse('Improper input upon_feedback')
        feedback = models.Feedback.objects.get(pk=feedback_id)

        if comment_id == '-1':
            new_comment = models.Comment(
                text=request.POST.get('text'),
                upon_feedback=feedback,
                author=user,
            )
        else:
            comment = models.Comment.objects.get(pk=comment_id)
            new_comment = models.Comment(
                text=request.POST.get('text'),
                upon_feedback=feedback,
                upon_comment=comment,
                author=user,
            )
        new_comment.save()
        return HttpResponse('OK')
    else:
        raise Http404('No GET interface has been defined for amplio.views.reply')


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
            populate_session(request, user)
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
            name_email_hash = md5((email + name).encode('utf-8')).hexdigest()
            password = form.cleaned_data.get('password')
            password_hash = md5(password.encode('utf-8')).hexdigest()
            user = models.User(
                name=name,
                email=email,
                name_email_hash=name_email_hash,
                password_hash=password_hash,
                post=choice_constants.STUDENT
            )
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


def subscribe(request):
    if request.method == 'POST':
        email = request.session.get('user_email', '')
        if len(email) == 0:
            raise Http404('You need to be logged in to access this interface')
        user = models.User.objects.get(email=email)
        comment_id = request.POST.get('id')
        comment = models.Comment.objects.get(pk=comment_id)
        if comment.subscribers.filter(email=email).exists():
            comment.subscribers.remove(user)
        else:
            comment.subscribers.add(user)
        comment.save()
        return HttpResponse(comment.subscribers.count())
    else:
        raise Http404('No GET interface has been defined for amplio.views.subscribe')


def terms(request):
    return render(request, 'amplio/terms.html')


def vote(request):
    if request.method == 'POST':
        email = request.session.get('user_email', '')
        if len(email) == 0:
            raise Http404('You need to be logged in to access this interface')
        user = models.User.objects.get(email=email)
        feedback_id = request.POST.get('id')
        feedback = models.Feedback.objects.get(pk=feedback_id)
        if feedback.patrons.filter(email=email).exists():
            feedback.patrons.remove(user)
        else:
            feedback.patrons.add(user)
        feedback.save()
        return HttpResponse(feedback.patrons.count())
    else:
        raise Http404('No GET interface has been defined for amplio.views.vote')
