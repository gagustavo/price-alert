from django.conf.urls import patterns, url

from price import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)