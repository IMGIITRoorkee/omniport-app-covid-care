from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from Covid_Care.serializers import LeadsSerializer, RequestsSerializer
from Covid_Care.models import Lead, Request


class SearchView(APIView):
    """
    """

    def get(self, request, *arigs, **kwargs):
        """
        """
        pin_code = request.query_params.get('p', None)
        resource = request.query_params.get('r', None)
        if pin_code is not None and resource is not None:
            try:
                leads = Lead.objects.filter(pin_code__startswith=pin_code[:2]).filter(
                    resource__resource_type=resource)
                requests = Request.objects.filter(pin_code__startswith=pin_code[:2]).filter(
                    resource__resource_type=resource)
                leadserializer = LeadsSerializer(
                    leads, many=True
                )
                requestserializer = RequestsSerializer(
                    requests, many=True
                )
            except:
                return Response(
                    data='Provide valid pin code and resource',
                    status=status.HTTP_404_NOT_FOUND
                )
            pin = int(pin_code)
            leadsIndex = {}
            requestsIndex = {}
            it = 0
            for i in leadserializer.data:
                leadsIndex[it] = abs(pin - i['pin_code'])
                it = it + 1
            it = 0
            for i in requestserializer.data:
                requestsIndex[it] = abs(pin - i['pin_code'])
                it = it + 1
            leadsIndex = {
                k: v for k,
                v in sorted(
                    leadsIndex.items(),
                    key=lambda item: item[1]
                )
            }
            requestsIndex = {
                k: v for k,
                v in sorted(
                    requestsIndex.items(),
                    key=lambda item: item[1]
                )
            }
            leadResponse = []
            requestResponse = []
            for i in leadsIndex:
                leadResponse.append(leadserializer.data[i])
            for i in requestsIndex:
                requestResponse.append(requestserializer.data[i])
            return Response(
                data={
                    'leads': leadResponse,
                    'requests': requestResponse
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data='Provide valid pin code and resource',
                status=status.HTTP_404_NOT_FOUND
            )
