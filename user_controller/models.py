from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager():
  pass

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_stuff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get("is_staff", False):
            raise ValueError("Superuser must gave is_staff=True.")

        if not extra_fields.get("is_superuser", False):
            raise ValueError("Superuser must gave is_staff=True.")

        return self.create_user(email,password, **extra_fields)


class User(AbstractBaseUser, PermissionError):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        super().full_clean()
        super().save(*args, **kwargs)
