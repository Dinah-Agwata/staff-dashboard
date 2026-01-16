from django.urls import path, include
from .views import staff_activity_dashboard
from django.contrib import admin

urlpatterns=[
    path(
        "staff/activity-dashboard/", staff_activity_dashboard, name="staff_activity_dashboard"
    ),
]