from rest_framework import viewsets, permissions
from covid_care.serializers import RequestsSerializer
from covid_care.models import Request
from covid_care.permissions import IsUploaderOrSafeMethods

all_http_method_names = viewsets.ModelViewSet.http_method_names


class RequestsViewSet(viewsets.ModelViewSet):
    """
    This viewset is used to handle the help requests.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsUploaderOrSafeMethods
    ]
    serializer_class = RequestsSerializer
    queryset = Request.objects.all()
    pagination_class = None
    http_method_names = [
        m for m in all_http_method_names if m not in [
            'put',
            'patch'
        ]
    ]
