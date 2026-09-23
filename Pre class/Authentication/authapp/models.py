from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=email
        )
        
        user.set_password(password)

        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)

    name = models.CharField(max_length=100)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email