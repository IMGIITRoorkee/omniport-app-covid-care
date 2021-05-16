import requests
from django.conf import settings
from django.template.loader import render_to_string

from emails.actions import email_push
from categories.models import Category


def send_request_email(person, request_data):
    """
    :param form:
    :return:
    """
    service = settings.DISCOVERY.get_app_configuration(
        'r_care'
    )
    app_category = Category.objects.get_or_create(
        name=service.nomenclature.verbose_name,
        slug=service.nomenclature.name,
    )
    category = Category.objects.get_or_create(
        name='Request',
        slug='r_care__request',
        parent=app_category[0]
    )
    pin = request_data['pin_code']
    URL = 'https://api.postalpincode.in/pincode/' + str(pin)
    r = requests.get(url=URL)
    try:
        district = r.json()[0]['PostOffice'][0]['District']
        state = r.json()[0]['PostOffice'][0]['State']
        body_text = render_to_string(
            'r_care/request_email.html', {'request': request_data, 'state': state, 'district': district})
    except Exception as e:
        body_text = render_to_string(
            'r_care/request_email.html', {'request': request_data})
    try:
        target_app_url = f'http://channeli.in/r_care/leads-and-requests/{pin}'
    except Exception as e:
        target_app_url = f'http://channeli.in/r_care/'

    try:
        email_push(
            subject_text=f'Emergency medical request created in R Care',
            body_text=body_text,
            category=category,
            has_custom_user_target=True,
            persons=person,
            target_app_name=service.nomenclature.name,
            target_app_url=target_app_url,
            send_only_to_subscribed_users=True,
        )
    except Exception as e:
        pass


def send_lead_email(person, lead_data):
    """
    :param form:
    :return:
    """

    service = settings.DISCOVERY.get_app_configuration(
        'r_care'
    )
    app_category = Category.objects.get_or_create(
        name=service.nomenclature.verbose_name,
        slug=service.nomenclature.name,
    )
    category = Category.objects.get_or_create(
        name='Lead',
        slug='r_care__lead',
        parent=app_category[0]
    )
    pin = lead_data['pin_code']
    URL = 'https://api.postalpincode.in/pincode/' + str(pin)
    r = requests.get(url=URL)
    try:
        district = r.json()[0]['PostOffice'][0]['District']
        state = r.json()[0]['PostOffice'][0]['State']
        body_text = render_to_string(
            'r_care/lead_email.html', {'lead': lead_data, 'state': state, 'district': district})
    except Exception as e:
        body_text = render_to_string(
            'r_care/lead_email.html', {'lead': lead_data})
    try:
        target_app_url = f'https://channeli.in/r_care/leads-and-requests/{pin}'
    except Exception as e:
        target_app_url = f'https://channeli.in/'
    try:
        email_push(
            subject_text='New lead added in R Care',
            body_text=body_text,
            category=category,
            has_custom_user_target=True,
            persons=person,
            target_app_name=service.nomenclature.name,
            target_app_url=target_app_url,
            send_only_to_subscribed_users=True,
        )
    except Exception as e:
        pass
