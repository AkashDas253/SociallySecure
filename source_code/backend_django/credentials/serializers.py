# serializers.py
from rest_framework import serializers
from .models import Credential

class CredentialSerializer(serializers.ModelSerializer):
    # Override the to_representation method to decrypt the credential_value
    def to_representation(self, instance):
        # Get the default representation from the parent method
        representation = super().to_representation(instance)
        
        # Decrypt the credential_value before returning it
        if 'credential_value' in representation:
            representation['credential_value'] = instance.decrypt_credential()
        
        return representation

    class Meta:
        model = Credential
        fields = ['id', 'user', 'credential_value', 'created_at']
        read_only_fields = ['id', 'created_at']
