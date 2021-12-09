from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class accountManager(BaseUserManager):
    def create_user(self, username=None, email=None, first_name=None, last_name=None, password=None):
        if not username: raise ValueError("User must have a login name.")
        if not email: raise ValueError("Users must have a email.")
        if not first_name: raise ValueError("Users must have a first name.")
        if not last_name: raise ValueError("Users must have a last name.")

        user = self.model(
            email=self.normalize_email(email), 
            username=username,
            
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username=None, email=None, first_name=None, last_name=None, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            
            username = username,
            password = password,

            first_name = first_name,
            last_name = last_name,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

class account(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email address', max_length=60, unique=True)
    username = models.CharField(verbose_name='Username', max_length=30, unique=True)
    first_name = models.CharField(verbose_name='First name', max_length=30)
    last_name = models.CharField(verbose_name='Last name', max_length=30)

    date_joined = models.DateTimeField(verbose_name='Date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last login', auto_now=True)

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = accountManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
    def __str__(self):
        return self.email