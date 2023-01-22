from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField( max_digits =12,decimal_places = 3)
    
    
    def __str__(self):
       return self.name
        