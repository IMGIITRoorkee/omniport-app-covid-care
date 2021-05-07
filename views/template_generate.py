from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from covid_care.serializers import RequestsSerializer, LeadsSerializer
from covid_care.utils.generate_card import store_request_template_image, store_lead_template_image


class RequestTemplateImageView(APIView):
    """
    Returns current user's help requests.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        request_id = request.query_params.get('id', None)
        if request_id is not None:
            request_template_link = store_request_template_image(request_id)

            return Response(
                {'template_link': request_template_link},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data='Provide valid Request ID',
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
            lead_template_link = store_lead_template_image(lead_id)

            return Response(
                {'template_link': lead_template_link},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data='Provide valid Lead ID',
                status=status.HTTP_404_NOT_FOUND
            )
