from formula_one.serializers.base import ModelSerializer
from covid_care.models import PlasmaDonor
from covid_care.serializers.requests import RequestsSerializer


class PlasmaDonorSerializer(ModelSerializer):
    """
    Details about the plasma donor
    """

    class Meta:
        model = PlasmaDonor
        fields = [
            'name',
            'contact',
            'other_contact',
            'blood_group',
            'tested_positive',
            'positive_when',
            'vaccinated',
            'pin_code',
            'address',
        ]
