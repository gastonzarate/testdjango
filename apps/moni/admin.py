"""Admin Moni"""

# Django
from django.contrib import admin

# Models
from apps.moni.models import Loan


class CustomLoanAdmin(admin.ModelAdmin):
    """Loan model admin."""

    list_display = ('first_name', 'last_name', 'amount', 'email', 'status')


admin.site.register(Loan, CustomLoanAdmin)
