from django.db import models

from django.core.validators import RegexValidator, MinValueValidator
from formula_one.models.base import Model
from Covid_Care.models.consts import categories


class Lead(Model):
    """
    Short Description about the model
    """

    category = models.CharField(
        max_length=63,
        choices=categories
    )
    name = models.CharField(
        max_length=255,
    )
    contact = models.CharField(
        max_length=63
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
    name = models.TextField(
        max_length=255,
        blank=True,
        null=True,
    )
    other_contact = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
