from django.db import models

# Create your models here.

class Product:
    product_id   = models.AutoField
    product_name = models.CharField(max_length=50)

    def __str__(self):
        return self.product_name