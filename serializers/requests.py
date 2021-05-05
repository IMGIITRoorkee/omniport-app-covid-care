from rest_framework import serializers
from formula_one.serializers.base import ModelSerializer
from omniport.utils import switcher
from covid_care.models import Request, RequestResource
from covid_care.serializers.resources import RequestResourceSerializer

AvatarSerializer = switcher.load_serializer('kernel', 'Person', 'Avatar')


class RequestsSerializer(ModelSerializer):
    """
    Details about the serializer
    """

    uploader = AvatarSerializer(
        read_only=True,
        fields=['id', 'full_name', 'roles']
    )
    resource = RequestResourceSerializer(many=True)
    status_display = serializers.ReadOnlyField(source='get_status_display')
    title = serializers.SerializerMethodField('get_title')

    def get_title(self, obj):
        request_title = ''
        resources = obj.resource.all()
        if len(resources) == 0:
            request_title = 'Request'
        else:
            for r in resources:
                request_title += f"{r.get_resource_type_display()}, "
            request_title = request_title[:-2]
            request_title += ' Request'
        return request_title

    class Meta:
        model = Request
        fields = [
            'pk',
            'patient_name',
            'age',
            'uploader',
            'contact',
            'other_contact',
            'pin_code',
            'address',
            'patient_spo2',
            'patient_ct_value',
            'status',
            'resource',
            'datetime_created',
            'status_display',
            'title',
        ]
        read_only = [
            'pk',
            'datetime_created',
            'uploader',
            'status_display',
            'title',
        ]

    def create(self, validated_data):
        resources_data = validated_data.pop('resource')
        person = self.context['request'].person
        request = Request.objects.create(
            **validated_data,
            uploader=person
        )
        for resource_data in resources_data:
            RequestResource.objects.create(
                request=request,
                **resource_data
            )
        return request
