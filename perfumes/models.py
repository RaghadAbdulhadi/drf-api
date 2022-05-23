from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    user_name = models.CharField(max_length=500)
    perfume_type = models.CharField(max_length=255)
    item_number = models.CharField(max_length=155, null=True, blank=True)

    def __str__(self):
        return self.email

class PurchaseItem(models.Model):
    type = models.CharField(max_length=100, null=True, blank=True)
    item_price = models.IntegerField(null=True, blank=True)
    item_review = models.TextField()
    item_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.type