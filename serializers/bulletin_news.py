from formula_one.serializers.base import ModelSerializer
from rest_framework import serializers
from Covid_Care.models import BulletinNew


class BulletinNewsSerializer(ModelSerializer):
    """
    Details about the Serializer
    """

    class Meta:
        model = BulletinNew
        fields = [
            'pk',
            'title',
            'description',
            'link',
            'images'
        ]
        read_only = [
            'title'
        ]
