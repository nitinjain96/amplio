from django.conf.urls import url

from amplio import views

app_name = 'amplio'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^sign-up/$', views.sign_up, name='sign_up'),
    url(r'^log-in/$', views.log_in, name='log_in'),
    url(r'^compose/$', views.compose, name='compose'),
]