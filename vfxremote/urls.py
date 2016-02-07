from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^(?P<chorelist_id>[0-9]+)/$', views.details, name='details'),
  url(r'^(?P<chorelist_id>[0-9]+)/vfxremote/$', views.chores, name='chores'),
  url(r'^(?P<chorelist_id>[0-9]+)/vfxremote/(?P<chore_id>[0-9]+)/$', views.choreDetails, name='choreDetails')
]