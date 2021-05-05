from rest_framework import viewsets, permissions
from covid_care.serializers import RequestsSerializer
from covid_care.models import Request
from covid_care.permissions import IsUploaderOrSafeMethods


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
