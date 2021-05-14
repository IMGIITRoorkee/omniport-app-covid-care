from formula_one.serializers.base import ModelSerializer
from r_care.models import PlasmaDonor
from r_care.serializers.requests import RequestsSerializer


class PlasmaDonorSerializer(ModelSerializer):
    """
    Details about the plasma donor
    """

    class Meta:
        model = PlasmaDonor
        fields = [
            'blood_group',
            'tested_positive',
            'positive_when',
            'vaccinated',
        ]
