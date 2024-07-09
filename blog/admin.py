from django.contrib import admin
from .models import Post, Comment, Like
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """

    list_display = ('title', 'slug', 'status')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Lists body, post and approved fields for display in admin
    """
    list_display = ('body', 'post', 'approved',)


admin.site.register(Like)
