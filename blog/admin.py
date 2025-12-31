from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'author', 'featured_image', 'content', 'excerpt', 'status')
    summernote_fields = ('content',)



class CommentAdmin(admin.ModelAdmin):
	list_display = ("post", "author", "approved", "created_on")
	list_filter = ("approved", "created_on")
	search_fields = ("post__title", "author__username", "body")


# Register your models here.
admin.site.register(Comment, CommentAdmin)


