from rest_framework import viewsets, permissions

from Covid_Care.serializers.donor import PlasmaDonorSerializer
from Covid_Care.models import PlasmaDonor


class PlasmaDonorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    """

    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = PlasmaDonorSerializer
    queryset = PlasmaDonor.objects.all()
