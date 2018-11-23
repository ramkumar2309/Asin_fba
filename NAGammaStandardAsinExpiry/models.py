from django.db import models

# Create your models here.
class Asin (models.Model):
    asin = models.CharField(max_length=250)
    product = models.CharField(max_length=500)

    def __str__(self):
        return self.asin + ' - ' + self.product

class AsinList(models.Model):
    asin = models.ForeignKey(Asin, on_delete=models.CASCADE)