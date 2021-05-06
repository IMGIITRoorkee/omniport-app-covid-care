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
    resource_type_display = serializers.ReadOnlyField(
        source='get_resource_type_display'
    )

    class Meta:
        model = RequestResource
        fields = [
            'request',
            'resource_type',
            'resource_type_display',
            'requirement',
            'patient_blood_group',
        ]
        read_only_fields = [
            'resource_type_display',
        ]


class LeadResourceSerializer(ModelSerializer):
    """
    Details about the serializer
    """
    resource_type_display = serializers.ReadOnlyField(
        source='get_resource_type_display'
    )

    class Meta:
        model = LeadResource
        fields = [
            'resource_type',
            'resource_type_display',
            'cost',
            'capacity',
            'description',
        ]
        read_only_fields = [
            'resource_type_display',
        ]
