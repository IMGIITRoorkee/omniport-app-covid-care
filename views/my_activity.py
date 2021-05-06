from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from covid_care.serializers import RequestsSerializer, LeadsSerializer


class MyRequestsView(APIView):
    """
    Returns current user's help requests.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        person = request.person

        requests = person.requests.all()
        response_data = RequestsSerializer(
            requests,
            many=True
        ).data

        return Response(
            data=response_data,
            status=status.HTTP_200_OK
        )


class MyLeadsView(APIView):
    """
    Returns current user's helpful leads.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        person = request.person

        leads = person.leads.all().exclude(resource__resource_type='plasma')
        response_data = LeadsSerializer(
            leads,
            many=True
        ).data

        return Response(
            data=response_data,
            status=status.HTTP_200_OK
        )


class MyPlasmaDonationsView(APIView):
    """
    Returns current user's plasma donations.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        person = request.person

        leads = person.leads.filter(resource__resource_type='plasma')
        response_data = LeadsSerializer(
            leads,
            many=True
        ).data

        return Response(
            data=response_data,
            status=status.HTTP_200_OK
        )


class MyActivityView(APIView):
    """
    Returns current user's requests, leads and plasma donations.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        person = request.person

        requests = RequestsSerializer(
            person.requests.all(),
            many=True
        ).data

        leads = LeadsSerializer(
            person.leads.all().exclude(resource__resource_type='plasma'),
            many=True
        ).data

        plasmaDonations = LeadsSerializer(
            person.leads.filter(resource__resource_type='plasma'),
            many=True
        ).data

        response_data = {
            'requests': requests,
            'leads': leads,
            'plasmaDonations': plasmaDonations
        }

        return Response(
            data=response_data,
            status=status.HTTP_200_OK
        )
