from rest_framework import viewsets, permissions
from Covid_Care.serializers import BulletinNewsSerializer
from Covid_Care.models import BulletinNew


class BulletinNewsViewSet(viewsets.ModelViewSet):
    """
    """

    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = BulletinNewsSerializer
    queryset = BulletinNew.objects.all()
    pagination_class = None
