from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserWallet(models.Model):
    user = models.OneToOneField(User, related_name="wallet", on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    amount = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.user} {self.balance}"
