from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

import swapper
from formula_one.models.base import Model
from r_care.constants import status


class Request(Model):
    """
    Short Description about the model
    """

    uploader = models.ForeignKey(
        to=swapper.get_model_name('kernel', 'Person'),
        related_name='requests',
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
    address = models.TextField()
    contact = models.CharField(
        max_length=63
    )
    patient_spo2 = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    patient_ct_value = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=50,
        choices=status,
        default='active'
    )
    other_contact = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self):
        """
        Short Description about the function
        """
        patient_name = self.patient_name
        return f'Request: Patient Name = {patient_name}'
