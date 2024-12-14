from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    opis = models.TextField()
    media_urls = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.title

#    (f'{self.id}, {self.title}, {self.price}, {self.category},'
  #   f' {self.sub_category}, {self.brand}, {self.opis} {self.media_urls}')