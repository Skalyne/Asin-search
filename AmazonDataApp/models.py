from django.db import models

# Create your models here.

class DataSheet (models.Model):
    id = models.AutoField(primary_key=True)
    asin=models.CharField(max_length=8)
    titulo=models.CharField(max_length=254)
    bullet_1=models.CharField(max_length=254)
    bullet_2=models.CharField(max_length=254)
    bullet_3=models.CharField(max_length=254)
    bullet_4=models.CharField(max_length=254)
    bullet_5=models.CharField(max_length=254)
    category=models.CharField(max_length=254)
    query_date=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name = "Busqueda Asin"
        verbose_name_plural = "Búsquedas Asin"

    def __str__(self):
        return self.asin


