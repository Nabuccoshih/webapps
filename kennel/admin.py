from django.contrib import admin
from django.utils import timezone

from .models import Kennel, Affixe


class KennelAdmin(admin.ModelAdmin):
	list_display = [
	    'surnom', 'nom', 'affixe', 'sexe', 'couleur', 'dob', 'age', 'puce'
	]


class AffixeAdmin(admin.ModelAdmin):
	list_display = ['nom']


admin.site.register(Kennel, KennelAdmin)
admin.site.register(Affixe, AffixeAdmin)
