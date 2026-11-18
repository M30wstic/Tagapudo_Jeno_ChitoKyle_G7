from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Administrator"
        FARMER = "FARMER", "Family Farmer"
        COOPERATIVE = "COOPERATIVE", "Farming Cooperative"
        BUYER = "BUYER", "Urban Buyer"

    email = models.EmailField("email address", unique=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.BUYER)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    organization = models.CharField(max_length=150, blank=True)
    profile_photo = models.ImageField(upload_to="profiles/", blank=True)

    def save(self, *args, **kwargs):
        self.email = self.email.strip().lower()
        if self.is_superuser:
            self.role = self.Role.ADMIN
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username