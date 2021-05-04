from django.db import models
from django.contrib.contenttypes import fields as contenttypes_fields
from django.contrib.contenttypes import models as contenttypes_models

from formula_one.models.base import Model
from Covid_Care.models import Lead, Request
from Covid_Care.models.consts import categories
from core.kernel.constants.biological_information import BLOOD_GROUPS


class RequestResource(Model):
    """
    Short Description about the model
    """

    request = models.ForeignKey(
        to=Request,
        on_delete=models.CASCADE,
        related_name='resource'
    )
    resource_type = models.CharField(
        max_length=63,
        choices=categories,
    )
    requirement = models.TextField(
        blank=True,
        null=True,
    )
    patient_blood_group = models.CharField(
        max_length=3,
        choices=BLOOD_GROUPS,
        blank=True,
        null=True,
    )

    def __str__(self):
        """
        Short Description about the function
        """
        resource_type = self.resource_type
        request = self.request
        return f'Request Resource: {resource_type}, {request}'


class LeadResource(Model):
    """
    Short Description about the model
    """

    lead = models.ForeignKey(
        to=Lead,
        on_delete=models.CASCADE,
        related_name='resource'
    )
    resource_type = models.CharField(
        max_length=63,
        choices=categories,
    )
    cost = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    capacity = models.TextField(
        blank=True,
        null=True,
    )
    description = models.TextField(
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        """
        Short Description about the function
        """
        resource_type = self.resource_type
        lead = self.lead
        return f'Lead Resource: {resource_type}, {lead}'
