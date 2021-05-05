from rest_framework import viewsets, permissions
from covid_care.serializers import PlasmaDonorSerializer
from covid_care.models import PlasmaDonor


class PlasmaDonorViewSet(viewsets.ModelViewSet):
    """
    """

    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = PlasmaDonorSerializer
    queryset = PlasmaDonor.objects.all()
    pagination_class = None
