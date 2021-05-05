from rest_framework import viewsets, permissions
from Covid_Care.models import RequestResource, LeadResource
from Covid_Care.serializers import (
    RequestResourceSerializer,
    LeadResourceSerializer
)
from Covid_Care.permissions import (
    IsRequestUploaderOrSafeMethods,
    IsLeadUploaderOrSafeMethods
)


class RequestResourcesViewSet(viewsets.ModelViewSet):
    """
    """

    permissions_classes = [
        permissions.IsAuthenticated,
        IsRequestUploaderOrSafeMethods
    ]
    serializer_class = RequestResourceSerializer
    queryset = RequestResource.objects.all()
    pagination_class = None


class LeadResourcesViewSet(viewsets.ModelViewSet):
    """
    """

    permissions_classes = [
        permissions.IsAuthenticated,
        IsLeadUploaderOrSafeMethods
    ]
    serializer_class = LeadResourceSerializer
    queryset = LeadResource.objects.all()
    pagination_class = None
