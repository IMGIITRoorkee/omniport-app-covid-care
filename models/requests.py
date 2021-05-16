import swapper
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

from formula_one.models.base import Model

from r_care.constants import status


class Request(Model):
    """
    Describes the details of a request registered.
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
        Return the string representation of the model
        :return: the string representation of the model
        """
        patient_name = self.patient_name
        return f'Request: Patient Name = {patient_name}'
