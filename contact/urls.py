from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_jetset_journal, name='contact'),
]
