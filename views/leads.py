import swapper
from rest_framework import viewsets, permissions
<<<<<<< HEAD
from r_care.serializers import LeadsSerializer
from r_care.models import Lead
from r_care.permissions import IsUploaderOrSafeMethods
from r_care.utils.send_email import send_lead_form
=======
from covid_care.serializers import LeadsSerializer
from covid_care.models import Lead
from covid_care.permissions import IsUploaderOrSafeMethods
from covid_care.utils.send_email import send_lead_email
>>>>>>> 3d0dd1a... Write template for emailing for leads and requests

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

    def create(self, request, *args, **kwargs):
        pin = str(request.data["pin_code"])
        location = swapper.load_model('formula_one', 'LocationInformation')
        l_i = location.objects.filter(postal_code__startswith=pin[:2])
        person = []
        for i in l_i:
            person += i.person.all()
        send_lead_email(person, request.data)
        response = super().create(request, *args, **kwargs)
        return response
