from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from omniport.utils import switcher

AvatarSerializer = switcher.load_serializer('kernel', 'Person', 'Avatar')


class PersonDataView(APIView):
    """
    Returns person location and contact information.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        person = request.person

        try:
            location_information = person.location_information.all()[0]
            contact_information = person.contact_information.all()[0]
            person_info = AvatarSerializer(
                person,
                fields=['id', 'full_name', 'roles']
            ).data
            person_information = {}
            for role in person_info['roles']:
                if role['role'] == 'Student':
                    person_information = {
                        'name': person_info['full_name'],
                        'role': 'Student',
                        'branch': role['data']['branch']['name'],
                        'degree': role['data']['branch']['degree']['name'].split(' - ')[0],
                        'year': role['data']['current_year'],
                    }
                elif role['role'] == 'FacultyMember':
                    person_information = {
                        'name': person_info['full_name'],
                        'role': 'Faculty',
                        'department': role['data']['department']['name'],
                    }
                else:
                    person_information = {
                        'name': person_info['full_name'],
                        'role': 'N.A.',
                        'department': 'N.A.',
                    }

        except:
            return Response(
                data="Couldn't find person location and contact information.",
                status=status.HTTP_404_NOT_FOUND
            )

        response_data = {
            'person_information': person_information,
            'location_information': {
                'address': location_information.address,
                'state': location_information.state,
                'postal_code': location_information.postal_code,
                'city': location_information.city,
                'country': location_information.get_country_display(),
            },
            'contact_information': {
                'phone': contact_information.primary_phone_number,
                'phone_alternate': contact_information.secondary_phone_number,
                'email': contact_information.email_address,
                'institute_webmail_address': contact_information.institute_webmail_address,
            },
        }

        return Response(
            data=response_data,
            status=status.HTTP_200_OK
        )
