from formula_one.serializers.base import ModelSerializer
from rest_framework import serializers
from Covid_Care.models import BulletinNew


class BulletinNewsSerializer(ModelSerializer):
    """
    Details about the Serializer
    """

    link = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = BulletinNew
        field = [
            'pk',
            'title',
            'description',
            'link',
            'images'
        ]
        read_only = [
            'title'
        ]
