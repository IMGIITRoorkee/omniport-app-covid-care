from rest_framework import serializers
from formula_one.serializers.base import ModelSerializer
from omniport.utils import switcher
from covid_care.models import Lead
from covid_care.serializers.resources import LeadResourceSerializer

AvatarSerializer = switcher.load_serializer('kernel', 'Person', 'Avatar')


class LeadsSerializer(ModelSerializer):
    """
    Details about the serializer
    """

    uploader = AvatarSerializer(
        read_only=True,
        fields=['id', 'full_name', 'roles']
    )
    upvote_count = serializers.ReadOnlyField(source='upvotes.count')
    downvote_count = serializers.ReadOnlyField(source='downvotes.count')
    resource = LeadResourceSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = Lead
        fields = [
            'pk',
            'name',
            'uploader',
            'contact',
            'pin_code',
            'upvote_count',
            'downvote_count',
            'address',
            'verification',
            'resource',
            'other_contact',
        ]
        read_only = [
            'name',
            'pin_code',
            'address',
        ]
