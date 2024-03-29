from django.contrib import admin
from .models import Post, Comment, Like, UserProfile
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


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    This class defines the admin configuration for the UserProfile model.
    It specifies the list display fields and search fields,
    and fieldsets for organizing user profile information, including personal
    information and contact details.
    """
    list_display = ['user', 'profile_picture', 'date_of_birth']
    search_fields = ['user__username', 'user__email', ]


# Register your models here.
admin.site.register(Comment)
admin.site.register(Like)
