from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import LoginForm, RegisterForm

def userView(request):
    context = {'user': request.user}
    return render(request, 'account/about_user.html', context)

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
    
    else: form = LoginForm()
    
    context = {'form': form}
    return render(request, 'account/login.html', context)

def registerView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")

    else: form = RegisterForm()

    context = {'form': form}
    return render(request, 'account/register.html', context)

def logoutView(request):
    logout(request)
    return redirect('login')