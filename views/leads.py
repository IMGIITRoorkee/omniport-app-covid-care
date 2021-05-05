from rest_framework import viewsets, permissions
from covid_care.serializers import LeadsSerializer
from covid_care.models import Lead
from covid_care.permissions import IsUploaderOrSafeMethods

all_http_method_names = viewsets.ModelViewSet.http_method_names


class LeadsViewSet(viewsets.ModelViewSet):
    """
    This viewset is used to handle the helpful leads.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsUploaderOrSafeMethods,
    ]
    serializer_class = LeadsSerializer
    queryset = Lead.objects.all()
    pagination_class = None
    http_method_names = [
        m for m in all_http_method_names if m not in [
            'put',
            'patch'
        ]
    ]
