from django.db import models

from formula_one.models.base import Model
from Covid_Care.models.consts import categories


class Resource(Model):
    """
    Short Description about the model
    """

    resource_type = models.CharField(
        max_length=50
        choices=categories
    )
    cost = models.PositiveIntegerField()
    capacity = models.CharField(
        max_length=15
    )
    requirement = models.TextField(
        max_length=127
    )
    patient_blood_group = models.CharField(
        max_length=2
    )
    description = models.TextField(
        max_length=255
    )
