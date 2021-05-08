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
    body_text = render_to_string(
        'covid_care/request_email.html', {'request': request_data})
    category = Category.objects.get_or_create(
        name=service.nomenclature.verbose_name,
        slug=service.nomenclature.name,
    )
    pin = request_data['pin_code']
    search_keyword = request_data['resource'][0]['resource_type']
    try:
        target_app_url = f'http://channeli.in/r_care/leads-and-requests/{pin}/{search_keyword}'
    except Exception as e:
        target_app_url = f'http://channeli.in/r_care/'
    print(target_app_url)
    try:
        email_push(
            subject_text=f'New request added on R-Care App',
            body_text=body_text,
            category=category,
            has_custom_user_target=True,
            persons=person,
            target_app_name=service.nomenclature.name,
            target_app_url=target_app_url,
            send_only_to_subscribed_users=True
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
    category = Category.objects.get_or_create(
        name=service.nomenclature.verbose_name,
        slug=service.nomenclature.name,
    )
    body_text = render_to_string(
        'covid_care/lead_email.html', {'lead': lead_data})
    pin = lead_data['pin_code']
    search_keyword = lead_data['resource'][0]['resource_type']
    try:
        target_app_url = f'https://channeli.in/r_care/leads-and-requests/{pin}/{search_keyword}'
    except Exception as e:
        target_app_url = f'https://channeli.in/'
    try:
        email_push(
            subject_text='New lead added on R Care App',
            body_text=body_text,
            category=category,
            has_custom_user_target=True,
            persons=person,
            target_app_name=service.nomenclature.name,
            target_app_url=target_app_url,
            send_only_to_subscribed_users=True
        )
    except Exception as e:
        pass
