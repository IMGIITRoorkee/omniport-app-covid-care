from rest_framework import viewsets, permissions
from Covid_Care.serializers import LeadsSerializer
from Covid_Care.models import Lead
from Covid_Care.permissions import IsUploaderOrSafeMethods


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
