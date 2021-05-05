from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters


from Covid_Care.serializers.resources import RequestResourceSerializer, LeadResourceSerializer
from Covid_Care.models import RequestResource, LeadResource


class RequestResourcesViewSet(viewsets.ModelViewSet):
    """
    """

    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = RequestResourceSerializer
    queryset = RequestResource.objects.all()


class LeadResourcesViewSet(viewsets.ModelViewSet):
    """
    """

    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = LeadResourceSerializer
    queryset = LeadResource.objects.all()
