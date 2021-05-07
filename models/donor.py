from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

from formula_one.models.base import Model
from covid_care.models import Lead
from core.kernel.constants.biological_information import BLOOD_GROUPS


class PlasmaDonor(Model):
    """
    Short Description about the model
    """

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
    lead = models.ForeignKey(
        to=Lead,
        on_delete=models.CASCADE,
        related_name='plasma_donor',
    )

    def __str__(self):
        """
        Short Description about the model
        """
        lead = self.lead
        blood_group = self.blood_group
        return f'Donor: Blood Group = {blood_group}, Lead = {lead}'
