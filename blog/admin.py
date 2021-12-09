from django.contrib import admin
from .models import BlogPost, FormPost

admin.site.register(BlogPost)
admin.site.register(FormPost)