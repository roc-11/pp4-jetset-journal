from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_jetset_journal, name='about'),
]