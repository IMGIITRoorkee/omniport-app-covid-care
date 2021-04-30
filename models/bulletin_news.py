from django.db import models
from tinymce.models import HTMLField

from formula_one.models.base import Model


class BulletinNews(Model):
    title = models.CharField(
        max_length=255
    )
    description = HTMLField(
        'Description',
    )
    link = models.URLField(
        max_length=200,
        many=True
    )
