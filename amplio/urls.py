from django.conf.urls import url

from amplio import views

app_name = 'amplio'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^browse/$', views.browse, name='browse'),
    url(r'^compose/$', views.compose, name='compose'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^edit-profile/$', views.edit_profile, name='edit-profile'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^search/$', views.search, name='search'),
    url(r'^sign-in/$', views.sign_in, name='sign_in'),
    url(r'^sign-up/$', views.sign_up, name='sign_up'),
    url(r'^sign-out/$', views.sign_out, name='sign_out'),
    url(r'^terms/$', views.terms, name='terms'),
    url(r'^vote/$', views.vote, name='vote'),
]