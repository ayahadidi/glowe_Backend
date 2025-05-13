from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUser(BaseUserManager):
    def create_user(self, email, password=None, **extra):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra):
        extra.setdefault('is_staff', True)
        extra.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra)


class User(AbstractBaseUser, PermissionsMixin):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=10)
    Email = models.EmailField(unique=True)
    Location = models.CharField(max_length=200)
    PromoCodeId=models.ForeignKey('Backend.PromoCode',on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = ['FirstName', 'LastName']

    objects = CustomUser()

    def __str__(self):
        return self.email

