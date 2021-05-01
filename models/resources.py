from django.db import models
from django.contrib.contenttypes import fields as contenttypes_fields
from django.contrib.contenttypes import models as contenttypes_models

from formula_one.models.base import Model
from Covid_Care.models.consts import categories
from core.kernel.constants.biological_information import BLOOD_GROUPS


class Resource(Model):
    """
    Short Description about the model
    """

    limit = models.Q(app_label='Covid_Care', model='request') | \
            models.Q(app_label='Covid_Care', model='lead')

    resource_type = models.CharField(
        max_length=50,
        choices=categories,
    )
    cost = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    capacity = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )
    requirement = models.TextField(
        max_length=127,
        blank=True,
        null=True,
    )
    patient_blood_group = models.CharField(
        max_length=3,
        choices=BLOOD_GROUPS,
        blank=True,
        null=True,
    )
    description = models.TextField(
        max_length=255,
        blank=True,
        null=True,
    )

    # Relationship with resource for entity
    entity_content_type = models.ForeignKey(
        to=contenttypes_models.ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=limit,
    )
    entity_object_id = models.PositiveIntegerField()
    resource_for = contenttypes_fields.GenericForeignKey(
        ct_field='entity_content_type',
        fk_field='entity_object_id',
    )
