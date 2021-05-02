from formula_one.serializers.base import ModelSerializer

from Covid_Care.models import PlasmaDonor
from Covid_Care.serializers.requests import RequestsSerializer


class PlasmaDonorSerializer(ModelSerializer):
    """
    Details about the serializer
    """

    request = RequestsSerializer(
        fields=[
            'pk',
            'patient_name',
            'contact',
            'pin_code',
            'address'
        ]
    )

    class Meta:
        model = PlasmaDonor
        fields = [
            'pk',
            'name',
            'contact',
            'blood_group',
            'tested_positive',
            'positive_when',
            'vaccinated',
            'pin_code',
            'address',
            'request',
            'other_contact',
        ]
        read_only = [
            'name',
            'contact',
            'blood_group',
            'tested_positive',
            'pin_code',
            'address',
        ]
