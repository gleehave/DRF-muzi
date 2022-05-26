from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models

from core.timestamp import TimeStampedModel

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        user = self.model(
            email    = self.normalize_email(email),
            username = username,
            **extra_fields
        )
        user.set_password(password)
        user.is_superuser = False
        user.save(using = self._db)

        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self.create_user(
            email    = self.normalize_email(email),
            username = username,
            password = password,
            **extra_fields
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    username     = models.CharField(max_length=254)
    email        = models.EmailField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=50)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True