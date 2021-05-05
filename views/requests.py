from rest_framework import viewsets, permissions
from Covid_Care.serializers import RequestsSerializer
from Covid_Care.models import Request
from Covid_Care.permissions import IsUploaderOrSafeMethods


class RequestsViewSet(viewsets.ModelViewSet):
    """
    """

    permissions_classes = [
        permissions.IsAuthenticated,
        IsUploaderOrSafeMethods
    ]
    serializer_class = RequestsSerializer
    queryset = Request.objects.all()
    pagination_class = None
