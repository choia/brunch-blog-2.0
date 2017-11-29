from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import PostForm
from .models import Post


'''Main View Page'''
def post_home(request):
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


'''Create Post Page'''
@login_required
def post_create(request):
	if not request.user.is_superuser:
		raise Http404

	if request.method != 'POST':
		form = PostForm()
	else:
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blog:post_home'))

	context = {
		"form": form
	}

	return render(request, 'forms.html', context)


'''Detailed Post Page'''
def post_detail(request, id):
	instance = get_object_or_404(Post, id=id)
	if instance.draft:	
		if not request.user.is_superuser:
			raise Http404
	context = {
		"instance": instance,
	}

	return render(request, 'detail.html', context)


'''Update Post Page'''
@login_required
def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	if request.method != 'POST':
		form = PostForm(instance=instance)
	else:	
		form = PostForm(request.POST, request.FILES, instance=instance)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"form": form,
	}

	return render(request, 'forms.html', context)


'''Delete Post Page'''
@login_required
def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect('blog:post_home')


'''Logout the user'''
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('blog:post_home'))