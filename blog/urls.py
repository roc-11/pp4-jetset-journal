from django.contrib.auth.views import LoginView
from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add/', views.add_blog_post, name='add_blog_post'),
    path('edit/<slug:slug>/', views.edit_blog_post, name='edit_blog_post'),
    path('delete/<slug:slug>/', views.delete_blog_post, name='delete_blog_post'),  # noqa
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
