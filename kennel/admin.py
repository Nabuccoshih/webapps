from django.contrib import admin
from django.utils import timezone

from .models import Chien, Affixe


class ChienAdmin(admin.ModelAdmin):
	list_display = [
	    'surnom', 'nom', 'affixe', 'sexe', 'couleur', 'dob', 'age', 'puce'
	]


class AffixeAdmin(admin.ModelAdmin):
	list_display = ['nom']


admin.site.register(Chien, ChienAdmin)
admin.site.register(Affixe, AffixeAdmin)
