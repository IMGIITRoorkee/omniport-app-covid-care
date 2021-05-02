from rest_framework import viewsets, permissions

from Covid_Care.serializers.leads import LeadsSerializer
from Covid_Care.models import Lead


class LeadsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    """

    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = LeadsSerializer
    queryset = Lead.objects.all()
