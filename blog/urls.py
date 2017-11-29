from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	#POST
	url(r'^$', views.post_home, name='post_home'),
	url(r'^create/$', views.post_create, name='post_create'),					
	url(r'^posts/(?P<id>\d+)$', views.post_detail, name='post_detail'),			
	url(r'^posts/(?P<id>\d+)/edit/$', views.post_update, name='post_update'),	
	url(r'^posts/(?P<id>\d+)/delete/$', views.post_delete, name='post_delete'),	
	#LOGIN
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='user_login'),
	url(r'^logout/$', views.logout_view, name='user_logout'),
]