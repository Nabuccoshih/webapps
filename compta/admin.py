from django.contrib import admin
from django.db.models import Sum
from .models import Categorie, Operation, Direction


class CategorieAdmin(admin.ModelAdmin):
    list_display = ['libelle']


class OperationAdmin(admin.ModelAdmin):

    list_display = [
        'date', 'libelle', 'moyen_paiement', 'categorie', 'montant_devise',
        'pointage'
    ]

    list_filter = ['categorie', 'moyen_paiement']

    actions = None

    def montant_devise(self, obj):
        return f"{obj.montant} €"

    def total_montant(self, obj):
        categorie = obj.categorie
        total = Operation.objects.filter('Alimentation').aggregate(
            Sum('montant'))['montant__sum'] or 0
        return total

class DirectionAdmin(admin.ModelAdmin):
    list_display = ['debit', 'credit']

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Operation, OperationAdmin)
admin.site.register(Direction, DirectionAdmin)