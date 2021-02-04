"""URL Configuration """
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Static
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    # Exchange app
    path('', include(('apps.moni.urls', 'moni'), namespace='moni')),
    # Users app
    path('', include(('apps.users.urls', 'users'), namespace='users')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
