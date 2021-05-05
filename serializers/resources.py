from rest_framework import serializers
from formula_one.serializers.base import ModelSerializer
from covid_care.models import (
    LeadResource,
    RequestResource,
)


class RequestResourceSerializer(ModelSerializer):
    """
    Details about the serializer
    """

    class Meta:
        model = RequestResource
        fields = [
            'pk',
            'request',
            'resource_type',
            'requirement',
            'patient_blood_group',
        ]
        read_only = [
            'request',
            'resource_type',
            'patient_blood_group',
        ]


class LeadResourceSerializer(ModelSerializer):
    """
    Details about the serializer
    """

    class Meta:
        model = LeadResource
        fields = [
            'pk',
            'lead',
            'resource_type',
            'cost',
            'capacity',
            'description',
        ]
        read_only = [
            'lead',
            'resource_type',
            'description',
        ]
