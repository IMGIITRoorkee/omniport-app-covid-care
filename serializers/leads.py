from formula_one.serializers.base import ModelSerializer
from omniport.utils import switcher
from Covid_Care.models import Lead
from Covid_Care.serializers.resources import LeadResourceSerializer 

AvatarSerializer = switcher.load_serializer('kernel', 'Person', 'Avatar')


class LeadsSerializer(ModelSerializer):
    """
    Details about the serializer
    """

    uploader = AvatarSerializer(
        read_only=True,
        fields=['id', 'full_name']
    )
    upvotes = AvatarSerializer(
        read_only=True,
        fields=['id', 'full_name'],
        many=True
    )
    downvotes = AvatarSerializer(
        read_only=True,
        fields=['id', 'full_name'],
        many=True
    )
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
            'upvotes',
            'downvotes',
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
