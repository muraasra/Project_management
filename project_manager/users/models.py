from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("manager", "Manager"),
        ("developer", "Developer"),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="developer")

    # Ajout des `related_name` pour éviter le conflit
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  # Un nouveau nom unique
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # Un nouveau nom unique
        blank=True
    )
