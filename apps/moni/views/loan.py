"""Loan views."""

# Django Rest Framework
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination

# Filters
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from rest_framework.permissions import IsAuthenticated, AllowAny

# Models
from apps.moni.models import Loan

# Serializers
from apps.moni.serializers import LoanSerializer


# Paginators
class Paginator(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


# Viewset
class LoanViewSet(mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """Loan view set"""

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    pagination_class = Paginator

    # Filters
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('dni', 'first_name', 'last_name', 'email')
    filterset_fields = ('status', 'gender')

    def get_permissions(self):
        """Restrict list and update to authenticated only."""
        permissions = []
        if self.action in ['update', 'partial_update', 'list', 'delete']:
            permissions.append(IsAuthenticated)
        if self.action == 'create':
            permissions.append(AllowAny)
        else:
            permissions.append(IsAuthenticated)
        return [permission() for permission in permissions]
