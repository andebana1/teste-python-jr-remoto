from rest_framework import serializers

from api import models

class OrganizationSerializer(serializers.ModelSerializer):
    login = serializers.CharField(max_length=255)
    class Meta:
        model = models.Organization
        fields = "__all__"

    def create(self, validated_data):
        org = models.Organization(**validated_data)
        org.save()
        return org