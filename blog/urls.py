from django.conf.urls import url
from . import views

urlpatterns = [
	#POST
	url(r'^$', views.post_home, name='post_home'),	
	#LOGIN
	url(r'^logout/$', views.logout_view, name='user_logout'),
]