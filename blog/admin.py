from django.contrib import admin
from django.db import models
from markdownx.widgets import AdminMarkdownxWidget
from .models import Post


class PostAdmin(admin.ModelAdmin):
	list_display = ["__str__", "date_added", "date_updated"]

	formfield_overrides = {
		models.TextField: {'widget': AdminMarkdownxWidget},
	}

	class Meta:
		model = Post

		
admin.site.register(Post, PostAdmin)

