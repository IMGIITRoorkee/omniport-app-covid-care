from django.urls import path, include
from rest_framework import routers

from r_care.views import *

app_name = 'r_care'

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
    path('my-activity', MyActivityView.as_view(), name='my_activity'),
    path('my-requests', MyRequestsView.as_view(), name='my_requests'),
    path('my-leads', MyLeadsView.as_view(), name='my_leads'),
    path('my-plasma-donations', MyPlasmaDonationsView.as_view(),
         name='my_plasma_donations'),
    path('request-template', RequestTemplateImageView.as_view(),
         name='request_template'),
    path('lead-template', LeadTemplateImageView.as_view(),
         name='lead_template'),
    path('', include(router.urls)),
]
