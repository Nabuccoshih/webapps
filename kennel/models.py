from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from dateutil.relativedelta import relativedelta


class Affixe(models.Model):
	nom = models.CharField(max_length=100)

	def __str__(self):
		return str(self.nom)


class Kennel(models.Model):

	def validate_puce(value):
		if len(str(value)) != 18:
			raise ValidationError(
			    'Le champ puce doit contenir exactement 18 caractères.')

	SEXE_CHOICES = (
	    ('M', 'Mâle'),
	    ('F', 'Femelle'),
	)

	COLOR_CHOICES = (
		('N', 'Noir'), ('NB', 'Noir et Blanc'),
	    ('TC', 'Tricolore'), ('DB', 'Doré et Blanc'))

	nom = models.CharField(max_length=255)
	affixe = models.ForeignKey(Affixe,
							on_delete=models.CASCADE,
							default=None)
	surnom = models.CharField(max_length=50)
	sexe = models.CharField(max_length=1,
							choices=SEXE_CHOICES,
							default='M')
	couleur = models.CharField(max_length=2,
	                        choices=COLOR_CHOICES,
	                        default='TC')
	dob = models.DateField()
	puce = models.CharField(max_length=18,
							validators=[validate_puce])

	def __str__(self):
		return str(self.surnom)

	def age(self):
		if self.dob:
			today = timezone.localdate()
			delta = relativedelta(today, self.dob)
			years = delta.years
			months = delta.months
			days = delta.days
			age_string = ""
			if years > 0:
				age_string += f"{years} {'an' if years > 1 else 'ans'}, "
			if months > 0:
				age_string += f"{months} {'mois' if months > 1 else 'mois'}, "
			if days > 0:
				age_string += f"{days} {'jour' if days > 1 else 'jours'}"
			return age_string.strip(', ')
		else:
			return None

	age.short_description = 'Âge'
