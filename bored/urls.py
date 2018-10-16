from django.conf.urls import url

from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    url(r'^$', views.HomeView, name='home'),
    #url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    
    url(r'^about$', views.AboutView.as_view(), name='about'),
    url(r'^front$', views.FrontView.as_view(), name='front'),
    url(r'^profile$', views.ProfileView.as_view(), name='profile'),
    url(r'^create$', views.createView, name='Create'),
    url(r'^profile/(?P<id>\d+)/edit/$', views.editView, name='update'),
    url(r'^profile/(?P<id>\d+)/delete/$', views.deleteView, name='delete'),
    url(r'^(?P<id>\d+)/$', views.post_detail,name='detail'),
    url(r'^profile/(?P<id>\d+)/$', views.profile_detail,name='profile_detail'),
]