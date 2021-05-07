import swapper
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from covid_care.serializers import RequestsSerializer
from covid_care.models import Request
from covid_care.permissions import IsUploaderOrSafeMethods
from covid_care.utils.send_email import send_request_form
from covid_care.constants.status import status as status_choices

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

    def update(self, request, *args, **kwargs):
        request_id = kwargs['pk']
        new_status = request.data.get('status', None)
        try:
            req = Request.objects.get(id=request_id)
            if new_status is None:
                return Response(
                    data='Status not provided.',
                    status=status.HTTP_400_BAD_REQUEST
                )
            if new_status not in [s[0] for s in status_choices]:
                return Response(
                    data='Invalid status.',
                    status=status.HTTP_400_BAD_REQUEST
                )
            req.status = new_status
            req.save()
        except:
            return Response(
                data='Request not found.',
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            data='Status updated.',
            status=status.HTTP_200_OK
        )
