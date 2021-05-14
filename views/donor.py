from rest_framework import viewsets, permissions
from r_care.serializers import PlasmaDonorSerializer
from r_care.models import PlasmaDonor
from r_care.permissions import IsLeadUploaderOrSafeMethods


class PlasmaDonorViewSet(viewsets.ModelViewSet):
    """
    Plasma donor information.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsLeadUploaderOrSafeMethods
    ]
    serializer_class = PlasmaDonorSerializer
    queryset = PlasmaDonor.objects.all()
    pagination_class = None
