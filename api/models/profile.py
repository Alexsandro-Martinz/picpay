from decimal import Decimal
from django.db import models

class Profile(models.Model):
    class ProfileType(models.TextChoices):
        COMMON = "COMMON"
        MERCHANT = "MERCHANT"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    document = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=11, decimal_places=2, default=Decimal(0))
    profile_type = models.CharField(
        max_length=100,
        choices=ProfileType.choices,
    )
     
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'