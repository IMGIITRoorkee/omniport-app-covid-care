from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from covid_care.models import Lead


class LeadVoteView(APIView):
    """
    Used to upvote or downvote a lead.
    """

    def post(self, request, *args, **kwargs):
        person = request.person
        lead = request.data.get('lead', None)
        vote = request.data.get('vote', 'upvote')

        if lead is not None:
            try:
                lead = Lead.objects.get(id=lead)
            except:
                return Response(
                    data='Lead not found.',
                    status=status.HTTP_404_NOT_FOUND
                )

            if vote == 'upvote':
                lead.downvotes.remove(person)
                lead.upvotes.add(person)

            elif vote == 'downvote':
                lead.upvotes.remove(person)
                lead.downvotes.add(person)

            return Response(
                data=f"Lead {vote}d successfully.",
                status=status.HTTP_200_OK
            )

        else:
            return Response(
                data='Lead not provided.',
                status=status.HTTP_400_BAD_REQUEST
            )
