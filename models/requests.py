from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

from formula_one.models.base import Model
from Covid_Care.models.consts import categories


class Request(Model):
    """
    Short Description about the model
    """
    requirement = models.CharField(
        max_length=63,
        choices=categories
    )
    patient_name = models.CharField(
        max_length=255,
    )
    age = models.PositiveIntegerField()
    pin_code = models.PositiveIntegerField(
        validators=[
            RegexValidator(r'^[0-9]{3,9}$'),
            MinValueValidator(0),
        ],
    )
    address = models.CharField(
        max_length=255
    )
    contact = models.CharField(
        max_length=63
    )
    patient_spo2 = models.PositiveIntegerField(
        max_value=100
    )
    patient_ct_value = models.PositiveIntegerField(
        max_value=100
    )
    other_contact = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
