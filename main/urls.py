from django.contrib import admin
from django.urls import path

from .views import homeView, contactView

urlpatterns = [
    path('home/', homeView, name='home'),
    path('contact/', contactView, name='contact'),
]
