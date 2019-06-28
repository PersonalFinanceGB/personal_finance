from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = AbstractUser.username  
    #name = models.CharField(blank=False, max_length=255, U)

    def __str__(self):
        return self.email
