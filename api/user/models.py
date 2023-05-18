from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from datetime import timezone
# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)





class CustomUser(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=50,default = 'Anonymous')
    email = models.EmailField(max_length=250,unique= True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField('Is active', default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []
    objects = UserManager()
    phone = models.CharField(max_length=20,blank= True,null = True)
    gender = models.CharField(max_length=10,blank= True,null = True)

    session_token = models.CharField(max_length=10, default = 0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
