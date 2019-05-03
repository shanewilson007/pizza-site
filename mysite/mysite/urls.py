from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url, include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
]
