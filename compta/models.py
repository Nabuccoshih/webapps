from django.db import models
from django.utils import timezone
from kennel.models import Chien

MOY_PAIEM_CHOICES = (
    ('CB', 'Carte Bleue'),
    ('VRT', 'Virement'),
    ('ESP', 'Espèces'),
)

POINT_CHOICES = [
    ('oui', 'Oui'),
    ('non', 'Non'),
]


class Categorie(models.Model):
    libelle = models.CharField(max_length=255)

    def __str__(self):
        return str(self.libelle)


class Operation(models.Model):
    date = models.DateField(default=timezone.now)
    libelle = models.CharField(max_length=255)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    moyen_paiement = models.CharField(max_length=3,
                                      choices=MOY_PAIEM_CHOICES,
                                      default='CB')
    categorie = models.ForeignKey(Categorie,
                                  on_delete=models.SET_NULL,
                                  null=True)
    destination = models.ForeignKey(Chien,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    blank=True)

    pointage = models.CharField(max_length=3,
                                choices=POINT_CHOICES,
                                default='non')

    def __str__(self):
        return str(self.libelle)


class Direction(models.Model):
    debit = models.ForeignKey(Operation,
                              related_name='direct_debit',
                              on_delete=models.SET_NULL,
                              null=True)
    credit = models.ForeignKey(Operation,
                               related_name='direct_credit',
                               on_delete=models.SET_NULL,
                               null=True)
