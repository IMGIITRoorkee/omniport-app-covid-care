from formula_one.serializers.base import ModelSerializer
from omniport.utils import switcher
from Covid_Care.models import Request

AvatarSerializer = switcher.load_serializer('kernel', 'Person', 'Avatar')


class RequestsSerializer(ModelSerializer):
    """
    Details about the serializer
    """

    uploader = AvatarSerializer(
        read_only=True,
        fields=['id', 'full_name']
    )

    class Meta:
        model = Request
        fields = [
            'pk',
            'patient_name',
            'age',
            'uploader',
            'contact',
            'pin_code',
            'address',
            'patient_spo2',
            'patient_ct_value',
            'status',
            'other_contact',
        ]
        read_only = [
            'patient_name',
            'age',
            'pin_code',
            'address',  
        ] 
