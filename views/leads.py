from rest_framework import viewsets, permissions
from covid_care.serializers import LeadsSerializer
from covid_care.models import Lead
from covid_care.permissions import IsUploaderOrSafeMethods


class LeadsViewSet(viewsets.ModelViewSet):
    """
    """

    permissions_classes = [
        permissions.IsAuthenticated,
        IsUploaderOrSafeMethods
    ]
    serializer_class = LeadsSerializer
    queryset = Lead.objects.all()
    pagination_class = None
