import uuid
from django.db import models

# Create your models here.
# api/models.py

# api/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    manufacturer_id = models.CharField(max_length=50)
    product_sn = models.CharField(max_length=50)
    hash_code = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name 

from django.db import models

class AdminRegistration(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # Add other fields as needed
