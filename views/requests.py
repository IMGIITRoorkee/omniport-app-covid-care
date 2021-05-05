from rest_framework import viewsets, permissions

from Covid_Care.serializers.requests import RequestsSerializer
from Covid_Care.models import Request


class RequestsViewSet(viewsets.ModelViewSet):
    """
    """

    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = RequestsSerializer
    queryset = Request.objects.all()
