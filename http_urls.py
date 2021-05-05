from django.urls import path, include
from rest_framework import routers

from Covid_Care.views.bulletin_news import BulletinNewsViewSet
from Covid_Care.views.requests import RequestsViewSet
from Covid_Care.views.leads import LeadsViewSet
from Covid_Care.views.donor import PlasmaDonorViewSet
from Covid_Care.views.resources import RequestResourcesViewSet, LeadResourcesViewSet
from Covid_Care.views.hello_world import HelloWorld
from Covid_Care.views.search import SearchView

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
    path('search', SearchView.as_view(), name='search'),
    path('', include(router.urls)),
]
