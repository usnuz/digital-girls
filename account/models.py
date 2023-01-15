from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(blank=True, max_length=254, verbose_name='email address', unique=True)
    middle_name = models.CharField(max_length=100, blank=True)
    gender = models.IntegerField(choices=(
        (0, "Erkak"),
        (1, "Ayol")
    ), blank=True, null=True)
    status = models.IntegerField(default=0, choices=(
        (0, "Moderator"),
        (1, "Admin"),
    ))
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar/")

    class Meta(AbstractUser.Meta):
        verbose_name = 'User'
        verbose_name_plural = 'Users'

