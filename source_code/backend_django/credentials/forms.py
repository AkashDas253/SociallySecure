# forms.py
from django import forms
from .models import Credential

class CredentialForm(forms.ModelForm):
    class Meta:
        model = Credential
        fields = ['credential_value']
