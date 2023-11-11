from django.db import models
from decimal import Decimal

 
class Transactions(models.Model):
    amount = models.DecimalField(max_digits=11, decimal_places=2, default=Decimal(0))
    sender_profile_id = models.IntegerField()
    receiver_profile_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
   