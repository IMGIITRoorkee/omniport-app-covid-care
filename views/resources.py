from rest_framework import viewsets, permissions
from r_care.models import RequestResource, LeadResource
from r_care.serializers import (
    RequestResourceSerializer,
    LeadResourceSerializer
)
from r_care.permissions import (
    IsRequestUploaderOrSafeMethods,
    IsLeadUploaderOrSafeMethods
)


class RequestResourcesViewSet(viewsets.ModelViewSet):
    """
    Resouce of a help request.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsRequestUploaderOrSafeMethods
    ]
    serializer_class = RequestResourceSerializer
    queryset = RequestResource.objects.all()
    pagination_class = None


class LeadResourcesViewSet(viewsets.ModelViewSet):
    """
    Resource of a helpful lead.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsLeadUploaderOrSafeMethods
    ]
    serializer_class = LeadResourceSerializer
    queryset = LeadResource.objects.all()
    pagination_class = None
