from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls.resolvers import URLPattern
from django.conf.urls import url
from . import views





urlpatterns=[
    path('', views.home,name='home'),
]


