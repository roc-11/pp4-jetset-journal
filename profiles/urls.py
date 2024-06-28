from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add_to_wishlist/<slug:slug>', views.add_to_wishlist, name='user_wishlist'),
]
