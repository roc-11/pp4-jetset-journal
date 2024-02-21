from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here - Class Based View, PostList
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"
    paginate_by = 6

