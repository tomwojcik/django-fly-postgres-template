from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.contrib.postgres.fields import CIEmailField


class User(AbstractUser):
    email = CIEmailField(unique=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower("email"),
                name="user_email_ci_uniqueness",
            ),
        ]
