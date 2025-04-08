from django.db import models

class MarketNews(models.Model):
    title = models.CharField(max_length=255)
    source = models.CharField(max_length=100)
    url = models.URLField()
    published_date = models.DateTimeField()
    category = models.CharField(max_length=50)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_date']

class ConstructionIndex(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    reference_date = models.DateField()
    source = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['-reference_date']

class MaterialPrice(models.Model):
    material = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20)
    supplier = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    last_update = models.DateTimeField()

    class Meta:
        ordering = ['-last_update'] 