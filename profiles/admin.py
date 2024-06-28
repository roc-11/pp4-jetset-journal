from django.contrib import admin
from .models import UserProfile

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
# admin.site.register(UserProfile)