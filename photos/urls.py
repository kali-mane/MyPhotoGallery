from django.conf.urls import url
from django.contrib.auth import views as auth_views
from photos.forms import LoginForm
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),   
    url(r'^(home)/$', views.home, name='home'),
    url(r'^register/$', views.register, name="register"),
    url(r'^albums/$', views.albumsView.as_view(), name='albums'),
    url(r'^(contact)/$', views.contact, name='contact'),
    url(r'^login/$', auth_views.login, {'template_name':'photos/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page':'/photos'}, name='logout'),    
    url(r'^(?P<album_name>\w+)/$', views.random),

]

