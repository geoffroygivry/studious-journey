from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^newlist/$', views.newlist, name='newlist'),
  url(r'^(?P<chorelist_id>[0-9]+)/$', views.details, name='details'),
  url(r'^(?P<chorelist_id>[0-9]+)/chores/(?P<chore_id>[0-9]+)/$', views.choreDetails, name='choreDetails'),
  url(r'^(?P<chorelist_id>[0-9]+)/chores/(?P<chore_id>[0-9]+)/update/$', views.updatechore, name='updatechore')
]