from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from r_care.models import Request, Lead
from r_care.serializers import RequestsSerializer, LeadsSerializer
from r_care.utils.generate_card import (
    store_request_template_image,
    store_lead_template_image
)


class RequestTemplateImageView(APIView):
    """
    Returns current user's help requests.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        request_id = request.query_params.get('id', None)
        if request_id is not None:
            try:
                req = Request.objects.get(id=request_id)
            except:
                return Response(
                    data='Request not found.',
                    status=status.HTTP_404_NOT_FOUND
                )

            request_template_link = store_request_template_image(request_id)

            return Response(
                data={
                    'template_link': request_template_link
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data='Request not found.',
                status=status.HTTP_404_NOT_FOUND
            )


class LeadTemplateImageView(APIView):
    """
    Returns current user's help requests.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        lead_id = request.query_params.get('id', None)
        if lead_id is not None:
            try:
                lead = Lead.objects.get(id=lead_id)
            except:
                return Response(
                    data='Lead not found.',
                    status=status.HTTP_404_NOT_FOUND
                )

            lead_template_link = store_lead_template_image(lead_id)

            return Response(
                data={
                    'template_link': lead_template_link
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data='Lead not found.',
                status=status.HTTP_404_NOT_FOUND
            )
