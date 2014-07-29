from django.conf.urls import patterns, include, url
import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^users$', views.user_list, name='user_list'),
                       url(r'^(?P<myusername>\w+)/followers$', views.followers, name='followers'),
                       url(r'^(?P<myusername>\w+)/following$', views.following, name='following'),
                       
 )