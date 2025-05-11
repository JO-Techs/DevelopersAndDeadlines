"""
URL Configuration for Deadline Project

This module defines the root URL patterns for the entire project,
including admin URLs, app-specific URLs, and static file serving.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Root URL patterns for the project
urlpatterns = [
    # Django admin interface
    path('admin/', admin.site.urls),
    
    # Include all URLs from the deadline_app
    path('', include('deadline_app.urls')),
    
    # Django REST Framework authentication URLs
    path('api-auth/', include('rest_framework.urls')),
    
# Serve static files during development
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)