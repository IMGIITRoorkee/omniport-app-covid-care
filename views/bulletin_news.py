from rest_framework import viewsets, permissions

from Covid_Care.serializers.bulletin_news import BulletinNewsSerializer
from Covid_Care.models.bulletin_news import BulletinNew


class BulletinNewsViewSet(viewsets.ModelViewSet):
    """
    """

    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = BulletinNewsSerializer
    queryset = BulletinNew.objects.all()
