from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class  UserProfileManager(BaseUserManager):
    """Manager for users pofiles"""
    def create_user(self, name, email, password=None):
        """create a new user profile"""
        if not email:
            raise ValueError('users must have an email address.')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, name, email, password):
        """Create and save a new super user with details"""
        user = self.create_user(email, name, password)
        
        user.is_superuser = True
        user.is_staff = True
        
        user.save(using=self._db)
        
        return user 

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """docstring for UserProfile"""
    email = models.EmailField(max_length = 254, unique=True)
    name = models.CharField(max_length = 254)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        """used to get the full name"""
        return self.name
    
    def get_short_name(self):
        """used to get the short name"""
        return self.name
    
    def __str__(self):
        """django used this when to convert the object into string"""
        return self.email
