from formula_one.serializers.base import ModelSerializer
from Covid_Care.models import (
    Resource,
    Request,
    Lead
)
from Covid_Care.serializers import RequestsSerializer, LeadsSerializer
from rest_framework import serializers


class ResourceForTypeRelatedField(serializers.RelatedField):
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
    resource_for = ResourceForTypeRelatedField(read_only=True)

    class Meta:
        model = Resource
        fields = [
            'pk',
            'name',
            'uploader',
            'contact',
            'pin_code',
            'upvotes',
            'downvotes',
            'address',
            'verification',
            'resource_for',
            'other_contact',
        ]
        read_only = [
            'name',
            'pin_code',
            'address',
            'resource_for'
        ]
