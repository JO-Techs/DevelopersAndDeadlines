"""
URL Configuration for Deadline App

This module defines the URL patterns for the deadline app,
mapping URL paths to their corresponding views.
"""

from django.urls import path
from .views import HomePageView, DeadlineDataView

# URL patterns for the deadline app
urlpatterns = [
    # Root URL serves the main homepage
    path('', HomePageView.as_view(), name='home'),
    
    # API endpoint for fetching deadline data
    path('api/deadline-data/', DeadlineDataView.as_view(), name='deadline-data'),
]