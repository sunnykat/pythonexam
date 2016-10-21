from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^join/(?P<d_id>\d+)$', views.join, name='join'),
    url(r'^add$', views.add, name='add'),
    url(r'^destination/(?P<d_id>\d+)$', views.show, name='show'),
    url(r'^destination/create$', views.create, name='create'),


]
