from rest_framework import serializers

from core.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = (
            'id',
            'name',
            'create_date',
            'update_date',
        )
