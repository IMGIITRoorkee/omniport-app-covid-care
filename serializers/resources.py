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
            'request',
            'resource_type',
            'requirement',
            'patient_blood_group',
        ]


class LeadResourceSerializer(ModelSerializer):
    """
    Details about the serializer
    """

    class Meta:
        model = LeadResource
        fields = [
            'resource_type',
            'cost',
            'capacity',
            'description',
        ]
