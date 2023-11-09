from django.db import models

from . profile import Profile


class Transactions(models.Model):
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    sender_profile = models.ForeignKey(Profile)
    receiver_profile = models.ForeignKey(Profile)
    timestamp = models.DateTimeField(auto_created=True)
    