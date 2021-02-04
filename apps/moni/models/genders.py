"""Gender Model"""

# Django
from django.db import models

# Utils
from apps.utils.models import BaseModel


class Gender(BaseModel):
    name = models.CharField(max_length=20)
    slug_name = models.SlugField()

    def __str__(self):
        return self.slug_name
