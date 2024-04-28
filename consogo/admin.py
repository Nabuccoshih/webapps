from django.contrib import admin

from .models import Conso

## calcul conso => (litres de carburant X 100) / Kilomètres parcourus


class ConsoAdmin(admin.ModelAdmin):
	list_display = [
	    'date', 'kilometrage', 'prix_au_litre', 'volume',
	    'calculate_total_cost'
	]

	def calculate_total_cost(self, obj):
		if obj.kilometrage and obj.prix_au_litre and obj.volume:
			return "{:.2f}".format(((obj.volume * 100) / obj.kilometrage))
		else:
			return None

	calculate_total_cost.short_description = 'Conso. Moy.'


admin.site.register(Conso, ConsoAdmin)
