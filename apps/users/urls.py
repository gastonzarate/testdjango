"""Users URLs."""
# Django
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import users as user_views

router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='users')

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='moni:new_loan'), name='logout')

]
urlpatterns += router.urls
