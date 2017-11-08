from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from photos.forms import LoginForm

#from photos.views import ImagesViewList

app_name = ''

urlpatterns = [
#    url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),        
    url(r'^(home)/$', views.home, name='home'),
    url(r'^(contact)/$', views.contact, name='contact'),
    url(r'^login/$', auth_views.login, {'template_name':'photos/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page':'/photos'}, name='logout'),    
    #    url(r'^(Random)/$', views.random, name='random'),
    url(r'^(?P<album_name>\w+)/$', views.random),

#   url(r'^(?P<album_name>\w+)/$', views.RandomView.as_view()),
    

    
    
    
]

