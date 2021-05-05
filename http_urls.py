from django.urls import path, include
from rest_framework import routers

from Covid_Care.views import (
    BulletinNewsViewSet,
    RequestsViewSet,
    LeadsViewSet,
    PlasmaDonorViewSet,
    PersonDataView,
    LeadVoteView,
    RequestResourcesViewSet,
    LeadResourcesViewSet,
    SearchView,
)

app_name = 'Covid_Care'

router = routers.SimpleRouter()

router.register(r'bulletinNews', BulletinNewsViewSet, basename='bulletinNews')
router.register(r'request', RequestsViewSet, basename='request')
router.register(r'lead', LeadsViewSet, basename='lead')
router.register(r'donor', PlasmaDonorViewSet, basename='donor')
router.register(r'request_resource', RequestResourcesViewSet,
                basename='requestResource')
router.register(r'lead_resource', LeadResourcesViewSet,
                basename='leadResource')

urlpatterns = [
    path('person-data', PersonDataView.as_view(), name='person_data'),
    path('lead-vote', LeadVoteView.as_view(), name='lead_vote'),
    path('search', SearchView.as_view(), name='search'),
    path('', include(router.urls)),
]
