"""Gender views."""

# Django Rest Framework
from rest_framework import viewsets, mixins

# Permissions
from rest_framework.permissions import AllowAny

# Models
from apps.moni.models import Gender

# Serializers
from apps.moni.serializers import GenderSerilizer


# Viewset
class GenderViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Gender view set"""

    queryset = Gender.objects.all()
    serializer_class = GenderSerilizer

    def get_permissions(self):
        """No restrict to the list."""
        permissions = [AllowAny]
        return [permission() for permission in permissions]
