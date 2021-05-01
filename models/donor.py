from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

from formula_one.models.base import Model


class PlasmaDonor(Model):
    """
    Short Description about the model
    """

    name = models.CharField(
        max_length=127
    )
    contact = models.CharField(
        max_length=31
    )
    blood_group = models.CharField(
        max_length=3
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
    address = models.CharField(
        max_length=255
    )
    other_contact = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
