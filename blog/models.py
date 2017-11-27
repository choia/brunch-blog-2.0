from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField


class PostManager(models.Manager):
	def active(self, *args, **kwargs):
		return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

def upload_location(instance, filename):
	return "%s/%s" % (instance.id, filename)


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	categories = models.CharField(max_length=25)
	title = models.CharField(max_length=180)
	email = models.EmailField()
	content = MarkdownxField()
	draft = models.BooleanField(default=True)
	publish = models.DateField(auto_now=True, auto_now_add=False)
	date_added = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	image = models.ImageField(upload_to=upload_location, null=True, blank=True, height_field="height_field", width_field="width_field")
	objects = PostManager()


	def __str__(self):
		return self.title
