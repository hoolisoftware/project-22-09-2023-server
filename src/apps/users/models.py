from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from . roles import ROLES


class User(AbstractUser, PermissionsMixin):
    role = models.CharField('Роль', max_length=32, choices=ROLES)
