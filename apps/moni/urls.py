# Django
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# Rest
from rest_framework import routers

# ViewSets
from apps.moni.views import LoanViewSet, GenderViewSet

# Router Rest
router = routers.SimpleRouter()
router.register(r'loans', LoanViewSet, basename='loans')
router.register(r'genders', GenderViewSet, basename='genders')


urlpatterns = [
    path('lista/prestamos/',
         login_required(TemplateView.as_view(template_name='moni/list_loan.html')),
         name='list_loan'),
    path('', TemplateView.as_view(template_name='moni/new_loan.html'), name='new_loan')
]
urlpatterns += router.urls
