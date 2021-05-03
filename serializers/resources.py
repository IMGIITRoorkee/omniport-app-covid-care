from formula_one.serializers.base import ModelSerializer
from Covid_Care.models import (
    Resource,
    Request,
    Lead
)
from Covid_Care.serializers.requests import RequestsSerializer
from Covid_Care.serializers.leads import LeadsSerializer
from rest_framework import serializers


class ResourceForRelatedField(serializers.RelatedField):
    """

    """

    def to_representation(self, value):
        """

        """
        if isinstance(value, Request):
            serializer = RequestsSerializer(value)
        elif isinstance(value, Lead):
            serializer = LeadsSerializer(value)
        else:
            raise Exception('Unexpected Type of Field Provided.')

        return serializer.data


class ResourceSerializer(ModelSerializer):
    """
    Details about the serializer
    """
    resource_for = ResourceForRelatedField(read_only=True)
    entity_content_type = serializers.SlugRelatedField(
        slug_field='model',
        read_only=True
    )

    class Meta:
        model = Resource
        fields = [
            'pk',
            'resource_type',
            'cost',
            'capacity',
            'requirement',
            'patient_blood_group',
            'description',
            'resource_for',
            'entity_content_type',
        ]
        read_only = [
            'resource_type',
            'resource_for'
        ]
