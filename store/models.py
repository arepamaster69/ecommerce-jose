from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=80)
    description=models.TextField()
    price=models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.1)]
    )
    stock=models.PositiveIntegerField()
    image=models.ImageField(upload_to='static/products')

    def _str__(self):

        return self.name