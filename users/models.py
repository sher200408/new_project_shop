from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUserModel(AbstractUser):
    DoesNotExist = None
    email = models.EmailField(unique=True)
