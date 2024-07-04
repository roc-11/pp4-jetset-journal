from .models import Comment, Post
from .widgets import CustomClearableFileInput
from cloudinary.forms import CloudinaryFileField
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a post 
    """
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    """
    A form for store admins to add blog posts to the blog
    """
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('users_wishlist', 'likes',)
    
    #featured_image = CloudinaryFileField()
    featured_image =  CloudinaryFileField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

