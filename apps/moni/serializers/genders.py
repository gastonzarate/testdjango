"""Gender serializers"""

# Django REST Framework
from rest_framework import serializers

# Models
from apps.moni.models import Gender


class GenderSerilizer(serializers.ModelSerializer):
    """Gender Model Serializer"""

    class Meta:
        """Meta class"""
        model = Gender
        fields = ['name', 'slug_name']
        lookup_field = 'slug_name'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
