from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=1000, decimal_places=2)

    def __str__(self):
        return f"{self.id}-- {self.title}"
