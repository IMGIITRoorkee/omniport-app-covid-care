from django.db import models

from formula_one.models.base import Model
from core.kernel.constants.biological_information import BLOOD_GROUPS

from r_care.models import Lead, Request
from r_care.constants import categories


class RequestResource(Model):
    """
    Describes the details of a resource registered for a request.
    """

    # Many-one Foreignkey relation between RequestResource and Request model
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
        Return the string representation of the model
        :return: the string representation of the model
        """
        resource_type = self.resource_type
        request = self.request
        return f'Request Resource: {resource_type}, {request}'


class LeadResource(Model):
    """
    Describes the details of a resource registered for a lead.
    """
    # One-one Foreignkey relation between LeadResource and Lead model
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
        Return the string representation of the model
        :return: the string representation of the model
        """
        resource_type = self.resource_type
        lead = self.lead
        return f'Lead Resource: {resource_type}, {lead}'
