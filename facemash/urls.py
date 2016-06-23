from django.conf.urls import url
from django.contrib import admin
from .views import home,top
urlpatterns = [
	url(r'^$', home, name='home'),
    url(r'^top$',top,name='top')
 ]