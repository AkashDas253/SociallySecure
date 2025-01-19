# serializers.py
from rest_framework import serializers
from .models import Credential

class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = ['id', 'user', 'credential_value', 'created_at']
        read_only_fields = ['id', 'created_at']
