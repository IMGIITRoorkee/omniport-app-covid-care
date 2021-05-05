from rest_framework import viewsets, permissions
from covid_care.serializers import BulletinNewsSerializer
from covid_care.models import BulletinNew


class BulletinNewsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns all the bulletin information articles.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BulletinNewsSerializer
    queryset = BulletinNew.objects.all()
    pagination_class = None
