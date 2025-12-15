from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ("title", "author", "status", "created_on", "updated_on")
	list_filter = ("status", "created_on", "updated_on")
	search_fields = ("title", "content", "author__username")
	prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
	list_display = ("post", "author", "approved", "created_on")
	list_filter = ("approved", "created_on")
	search_fields = ("post__title", "author__username", "body")


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
