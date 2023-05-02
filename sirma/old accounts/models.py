from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager)
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token 
from django.conf import settings


# Create your models here.
 
class MyUserManager(BaseUserManager):
    def create_user(self,email,username,password):
        if not email:
            raise ValueError("user should have an email")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self,email,username,password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password
            
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)

        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True,)
    username = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now=True)
    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser =  models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email' #login with email
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin

@receiver(signal= post_save,sender= settings.AUTH_USER_MODEL)
def create_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)
