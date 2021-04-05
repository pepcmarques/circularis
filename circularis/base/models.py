from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.translation import gettext_lazy as _

# from circularis.base.common import BaseModel
from circularis.accounts.models import User


class ProvinceManager(models.Manager):

    def populate(self, recreate=False):
        provinces = [('AB', 'Alberta'),
                     ('BC', 'British Columbia'),
                     ('MB', 'Manitoba'),
                     ('NB', 'New Brunswick'),
                     ('NL', 'Newfoundland and Labrador'),
                     ('NS', 'Nova Scotia'),
                     ('NT', 'Northwest Territories'),
                     ('NU', 'Nunavut'),
                     ('ON', 'Ontario'),
                     ('PE', 'Prince Edward Island'),
                     ('QC', 'Quebec'),
                     ('SK', 'Saskatchewan'),
                     ('YT', 'Yukon')]

        if recreate:
            print("deleting data")
            self.delete()
        else:
            if self.all():
                print(f"There is data in {self.model.__name__}. Nothing to do.")
                return False

        for province in provinces:
            code, name = province
            self.create(code=code, name=name)
            print(f"Populating {self.model.__name__} model with: {code}, {name}")

        return True


class Province(models.Model):

    class ProvincesChoices(models.TextChoices):

        AB = 'AB', _('Alberta')
        BC = 'BC', _('British Columbia')
        MB = 'MB', _('Manitoba')
        NB = 'NB', _('New Brunswick')
        NL = 'NL', _('Newfoundland and Labrador')
        NS = 'NS', _('Nova Scotia')
        NT = 'NT', _('Northwest Territories')
        NU = 'NU', _('Nunavut')
        ON = 'ON', _('Ontario')
        PE = 'PE', _('Prince Edward Island')
        QC = 'QC', _('Quebec')
        SK = 'SK', _('Saskatchewan')
        YT = 'YT', _('Yukon')

    code = models.CharField(max_length=2, unique=True, choices=ProvincesChoices.choices, default=ProvincesChoices.BC)
    name = models.CharField(max_length=25)

    objects = ProvinceManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'provinces'


class AddressManager(models.Manager):

    def has_address(self, user):
        return True if self.filter(user=user.pk).first() else False

    def get_address_or_none_by_user(self, user):
        try:
            return self.get(user=user.id)
        except ObjectDoesNotExist:
            return None


class Address(models.Model):

    street = models.CharField(max_length=60, blank=False)
    unit = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=50, blank=False)
    province = models.ForeignKey(Province, to_field='code', blank=False, on_delete=models.DO_NOTHING)
    postal_code = models.CharField(max_length=8, blank=False)
    lat = models.FloatField(verbose_name=_(u'Latitude'))
    long = models.FloatField(verbose_name=_(u'Longitude'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = AddressManager()

    def __str__(self):
        return self.postal_code

    def to_str(self):
        return f"{self.street}, {self.city}, {self.province.name}, {self.postal_code}"

    class Meta:
        ordering = ['postal_code']
