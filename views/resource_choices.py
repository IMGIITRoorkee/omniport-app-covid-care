from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from r_care.constants import categories


class ResourceChoicesView(APIView):
    """
    Returns resource choices.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        response_data = categories

        return Response(
            data=response_data,
            status=status.HTTP_200_OK
        )
