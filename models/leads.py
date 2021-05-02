from django.db import models

import swapper
from django.core.validators import RegexValidator, MinValueValidator
from formula_one.models.base import Model
from Covid_Care.models.consts import verification


class Lead(Model):
    """
    Short Description about the model
    """

    uploader = models.ForeignKey(
        to=swapper.get_model_name('kernel', 'Person'),
        related_name='leads_uploader',
        on_delete=models.CASCADE,
    )

    upvotes = models.ManyToManyField(
        swapper.get_model_name('kernel', 'Person'),
        related_name='leads_upvotes',
        blank=True
    )
    downvotes = models.ManyToManyField(
        swapper.get_model_name('kernel', 'Person'),
        related_name='leads_downvotes',
        blank=True
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
    address = models.TextField()
    verification = models.CharField(
        max_length=50,
        choices=verification
    )
    other_contact = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self):
        """
        Short Description about the model
        """
        name = self.name
        verification = self.verification
        return f'Lead: Name = {name}, Verification = {verification}'