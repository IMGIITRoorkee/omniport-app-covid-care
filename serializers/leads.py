from rest_framework import serializers
from formula_one.serializers.base import ModelSerializer
from omniport.utils import switcher
from covid_care.models import Lead, LeadResource
from covid_care.serializers.resources import LeadResourceSerializer

AvatarSerializer = switcher.load_serializer('kernel', 'Person', 'Avatar')


class LeadsSerializer(ModelSerializer):
    """
    Details about the serializer
    """

    uploader = AvatarSerializer(
        read_only=True,
        fields=['id', 'full_name', 'roles']
    )
    upvote_count = serializers.ReadOnlyField(source='upvotes.count')
    downvote_count = serializers.ReadOnlyField(source='downvotes.count')
    resource = LeadResourceSerializer(many=True)
    verification_display = serializers.ReadOnlyField(
        source='get_verification_display'
    )
    title = serializers.SerializerMethodField('get_title')

    def get_title(self, obj):
        lead_title = ''
        resources = obj.resource.all()
        if len(resources) == 0:
            lead_title = 'Lead'
        else:
            for r in resources:
                lead_title += f"{r.get_resource_type_display()}, "
            lead_title = lead_title[:-2]
            lead_title += ' Lead'
        return lead_title

    class Meta:
        model = Lead
        fields = [
            'pk',
            'name',
            'uploader',
            'contact',
            'other_contact',
            'pin_code',
            'upvote_count',
            'downvote_count',
            'address',
            'verification',
            'resource',
            'datetime_created',
            'verification_display',
            'title',
        ]
        read_only_fields = [
            'pk',
            'datetime_created',
            'uploader',
            'verification_display',
            'title',
        ]

    def create(self, validated_data):
        resources_data = validated_data.pop('resource')
        person = self.context['request'].person
        lead = Lead.objects.create(
            **validated_data,
            uploader=person
        )
        for resource_data in resources_data:
            LeadResource.objects.create(
                lead=lead,
                **resource_data
            )
        return lead
