from django.contrib import admin
from django.db.models import Sum

from .models import Categorie, Operation


class CategorieAdmin(admin.ModelAdmin):
    list_display = ['libelle']


class OperationAdmin(admin.ModelAdmin):
    list_display = [
        'date', 'libelle', 'montant_devise', 'moyen_paiement', 'categorie',
        'pointage', 'total_montant'
    ]

    def montant_devise(self, obj):
        return f"{obj.montant} €"

    def total_montant(self, obj):
        total = Operation.objects.aggregate(Sum('montant'))['montant__sum']
        return total


admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Operation, OperationAdmin)
