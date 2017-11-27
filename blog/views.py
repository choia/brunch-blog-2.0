from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from .models import Post


'''Main View Page'''
def post_home(request):
	# return render(request, 'index.html')
	queryset_list = Post.objects.active().order_by('-id')
	if request.user.is_superuser:
		queryset_list = Post.objects.all().order_by('-id')

	paginator = Paginator(queryset_list, 6)
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context = {
		"queryset": queryset,
	}

	return render(request, 'index.html', context)


'''Logout the user'''
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('blog:post_home'))