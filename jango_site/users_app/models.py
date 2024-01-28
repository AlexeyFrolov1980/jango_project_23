from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class AppUser(AbstractUser):
    email = models.EmailField(unique=True)
    can_edit = models.BooleanField(default=False)