import swapper
from rest_framework import viewsets, permissions
from covid_care.serializers import RequestsSerializer
from covid_care.models import Request
from covid_care.permissions import IsUploaderOrSafeMethods
from covid_care.utils.send_email import send_request_form

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

    def create(self, request, *args, **kwargs):
        pin = str(request.data["pin_code"])
        location = swapper.load_model('formula_one', 'LocationInformation')
        l_i = location.objects.filter(postal_code__startswith=pin[:2])
        person = []
        for i in l_i:
            person += i.person.all()
        send_request_form(person, pin)
        response = super().create(request, *args, **kwargs)
        return response
