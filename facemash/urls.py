from django.conf.urls import url
from django.contrib import admin
from .views import home,top,add,incre
urlpatterns = [
	url(r'^$', home, name='home'),
    url(r'^top$',top,name='top'),
    url(r'^add$',add,name='add'),
    url(r'^calc/(?P<id>\d+)/$',incre,name="calc"),
 ]