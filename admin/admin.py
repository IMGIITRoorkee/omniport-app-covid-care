from django.contrib.admin.sites import AlreadyRegistered

from omniport.admin.site import omnipotence
from Covid_Care.models import (
    Request,
    Lead,
    LeadResource,
    RequestResource,
    PlasmaDonor,
    BulletinNew
)

models = [
    Request,
    Lead,
    LeadResource,
    RequestResource,
    PlasmaDonor,
    BulletinNew
]

# Register all models

for model in models:
    try:
        omnipotence.register(model)
    except AlreadyRegistered:
        # A custom ModelAdmin has already registered it
        pass
