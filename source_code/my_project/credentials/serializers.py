from rest_framework import serializers
from .models import Credential

class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = ['id', 'credential_value', 'created_at']
        read_only_fields = ['created_at']
