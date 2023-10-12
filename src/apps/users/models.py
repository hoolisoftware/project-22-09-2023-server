from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from . roles import ROLES


class User(AbstractUser, PermissionsMixin):
    role = models.CharField('Role', max_length=32, choices=ROLES, help_text='This fields defines what user capable to do') # noqa
