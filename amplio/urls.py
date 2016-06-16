from django.conf.urls import url

from amplio import views

app_name = 'amplio'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]