from django.shortcuts import redirect, render

from .models import BlogPost, FormPost
from .forms import CreateBlog, CreateForm

def readBlogView(request):#?
    context = {'blogs': BlogPost.objects.filter(status=1).order_by('-created_on')}
    return render(request, 'blog/read_blog.html', context)

def readSpecificBlogView(request, slug):#?
    context = {'blog': BlogPost.objects.get(slug=slug)}

    return render(request, 'blog/specific_blog.html', context)

def readFormView(request):#!
    context = {'forms': FormPost.objects.filter(status=1).order_by('-created_on')}
    return render(request, 'blog/read_form.html', context)

def readSpecificFormView(request, slug):
    context = {'form': FormPost.objects.get(slug=slug)}

    return render(request, 'blog/specific_form.html', context)

def createBlogView(request):#?
    if not request.user.is_authenticated: return redirect('login')
    if request.method == 'POST':
        form = CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()  
    else: form = CreateBlog()
    
    context = {'form': form}
    return render(request, 'blog/create_blog.html', context)

def createFormView(request):#!
    if not request.user.is_authenticated: return redirect('login')
    
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
        else: print(form)
    else: form = CreateForm()
    
    context = {'form': form}
    return render(request, 'blog/create_form.html', context)