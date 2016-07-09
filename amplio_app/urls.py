from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^amplio/', include('amplio.urls')),
    url(r'^$', include('amplio.urls')),
    url(r'^admin/', admin.site.urls),
]
