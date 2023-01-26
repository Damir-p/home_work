from django.db import models

# Create your models here.

class Fruit(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    price = models.DecimalField(decimal_places=10, max_digits=10)

    def __sts__(self):
        return self.name
    

