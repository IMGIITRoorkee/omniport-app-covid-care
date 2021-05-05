from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

from formula_one.models.base import Model
from covid_care.models import Lead
from core.kernel.constants.biological_information import BLOOD_GROUPS


class PlasmaDonor(Model):
    """
    Short Description about the model
    """

    name = models.CharField(
        max_length=127,
        unique=True
    )
    contact = models.CharField(
        max_length=31
    )
    blood_group = models.CharField(
        max_length=3,
        choices=BLOOD_GROUPS,
    )
    tested_positive = models.BooleanField(
        default=False
    )
    positive_when = models.DateField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
    )
    vaccinated = models.BooleanField(
        default=False
    )
    pin_code = models.IntegerField(
        validators=[
            RegexValidator(r'^[0-9]{3,9}$'),
            MinValueValidator(0),
        ],
    )
    address = models.TextField()
    lead = models.ForeignKey(
        to=Lead,
        on_delete=models.CASCADE,
        related_name='plasma_donor',
    )
    other_contact = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    def __str__(self):
        """
        Short Description about the model
        """
        name = self.name
        blood_group = self.blood_group
        return f'Donor: Name = {name}, Blood Group = {blood_group}'
