from django.contrib import admin
from .models import Categorie, Operation, Debit, Credit


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


class DebitAdmin(admin.ModelAdmin):
    list_display = ['debit']


class CreditAdmin(admin.ModelAdmin):
    list_display = ['credit']


admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Operation, OperationAdmin)
admin.site.register(Debit, DebitAdmin)
admin.site.register(Credit, CreditAdmin)
