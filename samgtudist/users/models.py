from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ADMIN = "admin"
    MODERATOR = "moderator"
    USER = "user"

    ROLE_CHOICES = (
        (ADMIN, "Admin"),
        (MODERATOR, "Moderator"),
        (USER, "User"),
    )

    role = models.CharField(
        "Роль",
        max_length=9,
        choices=ROLE_CHOICES,
        default=USER
    )

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_user(self):
        return self.role == self.USER
