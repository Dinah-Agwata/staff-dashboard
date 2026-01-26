from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone

class Organization(models.Model):
    name=models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__ (self):
        return self.name

class User(AbstractUser):
    ROLE_CHOICES=[
        ("caregiver","Caregiver"),
        ("alternate","Alternate"),
        ("rn","RN")
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username
    
    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"

class Event(models.Model):
    ROLE_CHOICES=[
        ("active","Active"),
        ("inactive","Inactive")
    ]
        
    name = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True)
    staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="events")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.status}"