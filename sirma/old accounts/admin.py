from django.contrib import admin
from .models import User,MyUserManager

# Register your models here.
admin.site.register([User])
