""" User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Utilities
from apps.utils.models import BaseModel


class User(BaseModel, AbstractUser):
    """ User model.

    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': _('A user with that email already exists.')
        }
    )
    is_verified = models.BooleanField(
                                    _("is verified"),
                                    help_text='Set to true when the user have verified its email address.',
                                    default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        """Return username."""
        return self.username
