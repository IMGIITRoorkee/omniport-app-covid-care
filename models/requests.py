from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

import swapper
from formula_one.models.base import Model
from Covid_Care.models.consts import status


class Request(Model):
    """
    Short Description about the model
    """

    uploader = models.ForeignKey(
        to=swapper.get_model_name('kernel', 'Person'),
        related_name='request_uploader',
        on_delete=models.CASCADE,
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
    patient_spo2 = models.PositiveIntegerField()
    patient_ct_value = models.PositiveIntegerField()
    status = models.CharField(
        max_length=50,
        choices=status
    )
    other_contact = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
