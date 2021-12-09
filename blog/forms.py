from django import forms
from .models import BlogPost, FormPost
 
# Creating a blog
class CreateBlog(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'thumbnail', 'slug', 'content', 'status', 'author']

# Creating a form
class CreateForm(forms.ModelForm):
    class Meta:
        model = FormPost
        fields = ['title', 'slug', 'content', 'status', 'author']