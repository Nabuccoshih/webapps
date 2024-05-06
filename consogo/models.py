from django.db import models


class Conso(models.Model):
    date = models.DateField()
    kilometrage = models.IntegerField()
    prix_au_litre = models.DecimalField(max_digits=4, decimal_places=3)
    volume = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return str(self.date)
