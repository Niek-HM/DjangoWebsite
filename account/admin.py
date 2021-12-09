from django.contrib import admin
from django.contrib.auth import get_user_model

from django.contrib.auth.admin import UserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import *

User = get_user_model()

class UserAdmin(UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['email', 'is_admin', 'is_staff', 'is_superuser']
    list_filter = ['is_admin'] # Last filter will be enormous if there are a lot of schools

    fieldsets = [ # Info seen in specific accounts
        ('General',         {'fields': ['username', 'password']}),
        ('Personal info',   {'fields': ['first_name', 'last_name']}),
        ('Permissions',     {'fields': ['is_admin', 'is_staff', 'is_superuser']}),
        ('Other',           {'fields': ['is_active']})
    ]

    add_fieldsets = [ # Info seen when creating a new account
        ('New account', {'classes': ('wide'), 'fields': ('username', 'password1', 'password2', 'first_name', 'last_name')})
    ]

    search_fields = ['email', 'username']
    ordering = ['email',]
    filter_horizontal = ()

admin.site.register(User, UserAdmin)