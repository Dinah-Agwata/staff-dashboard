from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class Organization(models.Model):
    name=models.CharField(max_length=100)

def __str__ (self):
    return self.name

class User(AbstractUser):
    ROLE_CHOICES=[
        ("caregiver","Caregiver"),
        ("alternate","Alternate"),
        ("rn","RN")
    ]

    role=models.CharField(max_length=20, choices=ROLE_CHOICES)
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE, null=True, blank=True)

def __str__(self):
        return self.username

class Event(models.Model):
    staff=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="events")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.staff}-{self.created_at}"