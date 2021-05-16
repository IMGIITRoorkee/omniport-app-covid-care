from django.db import models

from formula_one.models.base import Model
from core.kernel.constants.biological_information import BLOOD_GROUPS

from r_care.models import Lead


class PlasmaDonor(Model):
    """
    Describes the details of the Plasma Donor registered.
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
    # One-one Foreignkey relation between lead and plasma donor model
    lead = models.ForeignKey(
        to=Lead,
        on_delete=models.CASCADE,
        related_name='plasma_donor',
    )

    def __str__(self):
        """
         Return the string representation of the model
        :return: the string representation of the model
        """
        lead = self.lead
        blood_group = self.blood_group
        return f'Donor: Blood Group = {blood_group}, Lead = {lead}'
