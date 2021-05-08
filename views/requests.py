import swapper
from django.utils import timezone
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from r_care.serializers import RequestsSerializer
from r_care.models import Request
from r_care.permissions import IsUploaderOrSafeMethods
from r_care.utils.send_email import send_request_email
from r_care.constants.status import status as status_choices

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
        person = request.person
        person_requests = Request.objects.filter(uploader=person)
        if len(person_requests) != 0:
            last_request = person_requests.order_by('-datetime_created')[0]
            last_created_on = last_request.datetime_created
            time_delta = timezone.now() - last_created_on
            time_delta_minutes = time_delta.total_seconds() / 60

            if time_delta_minutes < 30:
                return Response(
                    data=f"Cannot create more than one request within 30 minutes.",
                    status=status.HTTP_429_TOO_MANY_REQUESTS
                )

        pin = str(request.data["pin_code"])
        location = swapper.load_model('formula_one', 'LocationInformation')
        l_i = location.objects.filter(postal_code__startswith=pin[:2])
        person = []
        for i in l_i:
            person += i.person.all()
        send_request_email(person, request.data)
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
