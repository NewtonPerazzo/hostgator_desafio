from django.db import models

# Create your models here.
class Dominio(models.Model):
    dominio = models.CharField(max_length=100, null=True, blank=True)
    available = models.BooleanField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    reason = models.CharField(max_length=100, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Dominio: {self.dominio}'