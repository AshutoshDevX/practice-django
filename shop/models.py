from django.db import models

# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500,default='No description available')
    add = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
            return self.name
    