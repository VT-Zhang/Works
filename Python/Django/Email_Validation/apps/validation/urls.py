from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit$', views.submit),
    url(r'^goback$', views.goback),
    url(r'^delete/(?P<id>\d+)$', views.delete),
]
