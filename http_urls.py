from django.urls import path, include
from rest_framework import routers

from covid_care.views import (
    BulletinNewsViewSet,
    RequestsViewSet,
    LeadsViewSet,
    PlasmaDonorViewSet,
    PersonDataView,
    LeadVoteView,
    RequestResourcesViewSet,
    LeadResourcesViewSet,
    SearchView,
    ResourceChoicesView,
)

app_name = 'covid_care'

router = routers.SimpleRouter()

router.register(r'bulletin', BulletinNewsViewSet, basename='bulletin')
router.register(r'request', RequestsViewSet, basename='request')
router.register(r'lead', LeadsViewSet, basename='lead')
router.register(r'donor', PlasmaDonorViewSet, basename='donor')
router.register(
    r'request-resource',
    RequestResourcesViewSet,
    basename='request_resource'
)
router.register(
    r'lead-resource',
    LeadResourcesViewSet,
    basename='lead_resource'
)

urlpatterns = [
    path('person-data', PersonDataView.as_view(), name='person_data'),
    path('lead-vote', LeadVoteView.as_view(), name='lead_vote'),
    path('search', SearchView.as_view(), name='search'),
    path('resource-choices', ResourceChoicesView.as_view(), name='resource_choices'),
    path('', include(router.urls)),
]
