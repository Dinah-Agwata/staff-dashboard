from django.contrib import admin
from .models import Event, Organization
from django.contrib.auth import get_user_model

User=get_user_model()

admin.site.register(Event)
admin.site.register(User)
admin.site.register(Organization)