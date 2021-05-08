from django.conf import settings

from emails.actions import email_push
from categories.models import Category


def send_request_form(person, pin_code):
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
    body_text = f'New request for region around {pin_code} is added.'
    target_app_url = f'https://channeli.in/'

    try:
        email_push(
            subject_text=f'New request added on Covid Care',
            body_text=body_text,
            category=category,
            has_custom_user_target=True,
            persons=person,
            target_app_name=service.nomenclature.name,
            target_app_url=target_app_url,
            # send_only_to_subscribed_users=True
        )
    except Exception as e:
        pass


def send_lead_form(person, pin_code):
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
    body_text = f'New lead for region around {pin_code} is added.'
    target_app_url = f'https://channeli.in/'

    try:
        email_push(
            subject_text=f'New lead added on Covid Care',
            body_text=body_text,
            category=category,
            has_custom_user_target=True,
            persons=person,
            target_app_name=service.nomenclature.name,
            target_app_url=target_app_url,
            # send_only_to_subscribed_users=True
        )
    except Exception as e:
        pass
