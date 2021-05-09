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
        'r_care/request_email.html', {'request': request_data})
    category = Category.objects.get_or_create(
        name=service.nomenclature.verbose_name,
        slug=service.nomenclature.name,
    )
    pin = request_data['pin_code']
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
        'r_care/lead_email.html', {'lead': lead_data})
    pin = lead_data['pin_code']
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
        )
    except Exception as e:
        pass
