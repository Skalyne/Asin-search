from django.db import models

# Create your models here.

class DataSheet (models.Model):
    asin=models.CharField(max_length=8)
    titulo=models.CharField(max_length=254)
    bullet_1=models.CharField(max_length=254)
    bullet_2=models.CharField(max_length=254)
    bullet_3=models.CharField(max_length=254)
    bullet_4=models.CharField(max_length=254)
    bullet_5=models.CharField(max_length=254)
    category=models.CharField(max_length=254)
    query_date=models.DateTimeField(auto_now_add=True)

