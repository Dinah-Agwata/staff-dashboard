from django.urls import path
from django.contrib import admin

from .views import staff_activity_dashboard


urlpatterns=[
    path(
        "staff/activity-dashboard/", staff_activity_dashboard, name="staff_activity_dashboard"
    ),
]