from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from dateutil.relativedelta import relativedelta

SEXE_CHOICES = (
    ('M', 'Mâle'),
    ('F', 'Femelle'),
)

COLOR_CHOICES = (('N', 'Noir'), ('NB', 'Noir et Blanc'), ('TC', 'Tricolore'),
                 ('DB', 'Doré et Blanc'))

POS_CHOICES = (
    ('P', 'Préfixe'),
    ('S', 'Suffixe'),
)


class Affixe(models.Model):
    nom = models.CharField(max_length=100)
    position = models.CharField(max_length=1, choices=POS_CHOICES, default='S')

    def __str__(self):
        return str(self.nom)


class Chien(models.Model):

    def validate_puce(value):
        if len(str(value)) != 18:
            raise ValidationError(
                'Le champ puce doit contenir exactement 18 caractères.')

    nom = models.CharField(max_length=255)
    affixe = models.ForeignKey(Affixe, on_delete=models.CASCADE, default=None)
    surnom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES, default='M')
    couleur = models.CharField(max_length=2,
                               choices=COLOR_CHOICES,
                               default='TC')
    dob = models.DateField()
    puce = models.CharField(max_length=18, validators=[validate_puce])

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


class Chiot(models.Model):
    nom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES, default='M')
    couleur = models.CharField(max_length=2,
                               choices=COLOR_CHOICES,
                               default='TC')

    def __str__(self):
        return str(self.nom)


class Client(models.Model):

    def validate_cp(value):
        if len(str(value)) != 5:
            raise ValidationError(
                'Le code postal doit contenir exactement 5 caractères numériques.'
            )

    def validate_tel(value):
        phone_regex = RegexValidator(
            regex=r'^(\+\d{2,3})? ?(\d{2} ?){4}\d{2}$',
            message=
            'Le numéro de téléphone doit être au format "01 23 45 67 89".')
        phone_regex(value)

    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    adresse = models.CharField(max_length=255)
    cp = models.CharField(max_length=5, validators=[validate_cp])
    ville = models.CharField(max_length=50)
    tel = models.CharField(max_length=14, validators=[validate_tel])
    email = models.EmailField(validators=[EmailValidator()])
    dobc = models.DateField()
    chiot_choisi = models.ForeignKey(Chiot,
                                     on_delete=models.CASCADE,
                                     default=None)

    def __str__(self):
        return str(self.nom)


class Portee(models.Model):
    nom = models.CharField(max_length=50)
    dob = models.DateField()
    pere = models.ForeignKey(Chien,
                             related_name='portees_pere',
                             on_delete=models.CASCADE,
                             default=None)
    mere = models.ForeignKey(Chien,
                             related_name='portees_mere',
                             on_delete=models.CASCADE,
                             default=None)
    chiot = models.ManyToManyField(Chiot)

    def __str__(self):
        return str(self.nom)
