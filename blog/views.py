from django.contrib.auth import logout
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse


'''Main View Page'''
def post_home(request):
	return render(request, 'index.html')


'''Logout the user'''
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('blog:post_home'))