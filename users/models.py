from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUserModel(AbstractUser):
    email = models.EmailField(unique=True)
