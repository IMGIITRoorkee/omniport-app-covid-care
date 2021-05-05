from rest_framework import viewsets, permissions
from Covid_Care.serializers import PlasmaDonorSerializer
from Covid_Care.models import PlasmaDonor


class PlasmaDonorViewSet(viewsets.ModelViewSet):
    """
    """

    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = PlasmaDonorSerializer
    queryset = PlasmaDonor.objects.all()
    pagination_class = None
