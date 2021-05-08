import os
import re
import json
import string
import requests
import tempfile

from django.conf import settings
from django.template.loader import render_to_string

from weasyprint import HTML
from r_care.models import Request, Lead
from django.http import HttpResponse


def store_request_template_image(request_id):
    """
    """

    # Model Data
    try:
        request = Request.objects.get(id=request_id)
    except Exception as e:
        return 'Link unavailable'
    URL = 'https://api.postalpincode.in/pincode/' + str(request.pin_code)
    r = requests.get(url=URL)
    try:
        district = r.json()[0]['PostOffice'][0]['District']
        state = r.json()[0]['PostOffice'][0]['State']
        html = render_to_string(
            'r_care/request.html', {'request': request, 'state': state, 'district': district})

    except Exception as e:
        html = render_to_string(
            'r_care/request.html', {'request': request})

    filtered_string = ''.join(
        filter(lambda x: x in string.printable, html))
    filtered_string = re.sub(
        u'[^\u0020-\uD7FF\u0009\u000A\u000D\uE000-\uFFFD\u10000-\u10FFFF]+', '',
        filtered_string
    )

    name = f'{request.patient_name}_{request_id}'
    request_image_folder = os.path.join(
        'r_care',
        'request_image'
    )
    destination = os.path.join(settings.MEDIA_ROOT, request_image_folder)
    if not os.path.exists(destination):
        os.makedirs(destination)

    media_dir = os.path.join(destination, f'{name}.png')
    HTML(string=filtered_string).write_png(media_dir)
    final_destiantion = os.path.join(request_image_folder, f'{name}.png')

    request_template_url = f"/media/{final_destiantion}"
    return request_template_url


def store_lead_template_image(lead_id):
    """
    """

    # Model Data
    try:
        lead = Lead.objects.get(id=lead_id)
    except Exception as e:
        return 'Link Unavailable'
    URL = 'https://api.postalpincode.in/pincode/' + str(lead.pin_code)
    r = requests.get(url=URL)
    try:
        district = r.json()[0]['PostOffice'][0]['District']
        state = r.json()[0]['PostOffice'][0]['State']
        html = render_to_string(
            'r_care/lead.html', {'lead': lead, 'state': state, 'district': district})
    except Exception as e:
        html = render_to_string(
            'r_care/lead.html', {'lead': lead})
    filtered_string = ''.join(
        filter(lambda x: x in string.printable, html))
    filtered_string = re.sub(
        u'[^\u0020-\uD7FF\u0009\u000A\u000D\uE000-\uFFFD\u10000-\u10FFFF]+', '',
        filtered_string
    )

    name = f'{lead.name}_{lead_id}'
    lead_image_folder = os.path.join(
        'r_care',
        'lead_image'
    )
    destination = os.path.join(settings.MEDIA_ROOT, lead_image_folder)
    if not os.path.exists(destination):
        os.makedirs(destination)

    media_dir = os.path.join(destination, f'{name}.png')
    HTML(string=filtered_string).write_png(media_dir)
    final_destiantion = os.path.join(lead_image_folder, f'{name}.png')

    lead_template_url = f"/media/{final_destiantion}"
    return lead_template_url
