from django.contrib import admin
from django.urls import path

from .views import readBlogView, readFormView, createBlogView, createFormView, readSpecificBlogView, readSpecificFormView

urlpatterns = [
    path('create_form/', createFormView, name='create_form'),
    path('create_blog/', createBlogView, name='create_blog'),
    path('read_blog/<slug:slug>/', readSpecificBlogView, name='read_specific_blog'),
    path('read_blog/', readBlogView, name='read_blog'),
    path('read_form/<slug:slug>/', readSpecificFormView, name='read_specific_form'),
    path('read_form/', readFormView, name='read_form'),
]