from django.contrib import admin
from .models import Conso


class ConsoAdmin(admin.ModelAdmin):
	list_display = ['date', 'kilometrage', 'prix_au_litre', 'volume']


admin.site.register(Conso, ConsoAdmin)
