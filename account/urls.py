from django.contrib import admin
from django.urls import path

from .views import userView, loginView, registerView, logoutView

urlpatterns = [
    path('me/', userView, name='user_info'),
    path('login/', loginView, name='login'),
    path('register/', registerView, name='register'),
    path('logout/', logoutView, name='logout')
]
