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
        blank=True
    )
    images = models.FileField(
        upload_to=UploadTo('r_care', 'r_care_files'),
        blank=True
    )

    def __str__(self):
        """
        Short Description about the model
        """
        name = self.title
        return f'Bulletin News: Name = {name}'