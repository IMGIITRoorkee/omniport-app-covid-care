from rest_framework import viewsets, permissions
from covid_care.serializers import PlasmaDonorSerializer
from covid_care.models import PlasmaDonor
from covid_care.permissions import IsLeadUploaderOrSafeMethods


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
