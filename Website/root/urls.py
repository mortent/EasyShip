from django.conf.urls import patterns, url

from root import views

urlpatterns = patterns('',
	url(r'^$', views.search, name='search'),
)