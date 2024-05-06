from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.utils import timezone

from .models import Chien, Affixe, Chiot, Client, Portee


class ChienAdmin(admin.ModelAdmin):
    list_display = [
        'surnom', 'nom', 'affixe', 'sexe', 'couleur', 'dob', 'age', 'puce'
    ]


class AffixeAdmin(admin.ModelAdmin):
    list_display = ['nom']


class ChiotAdmin(admin.ModelAdmin):
    list_display = ['nom', 'sexe', 'couleur']


class PorteeAdmin(admin.ModelAdmin):
    list_display = ['nom', 'dob', 'pere', 'mere']


class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'nom', 'prenom', 'adresse', 'cp', 'ville', 'tel', 'email', 'dobc',
        'chiot_choisi'
    ]


admin.site.register(Chien, ChienAdmin)
admin.site.register(Affixe, AffixeAdmin)
admin.site.register(Chiot, ChiotAdmin)
admin.site.register(Portee, PorteeAdmin)
admin.site.register(Client, ClientAdmin)
