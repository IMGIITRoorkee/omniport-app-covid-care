from django.db import models
from tinymce.models import HTMLField

from formula_one.models.base import Model
from formula_one.utils.upload_to import UploadTo


class BulletinNew(Model):
    title = models.CharField(
        max_length=255
    )
    description = HTMLField(
        'Description',
    )
    link = models.URLField(
        max_length=200,
        blank=True
    )
    images = models.FileField(
        upload_to=UploadTo('Covid_Care', 'covid_care_files'),
        blank=True
    )
