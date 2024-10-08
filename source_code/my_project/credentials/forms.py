from django import forms
from .models import Credential

class CredentialForm(forms.ModelForm):
    class Meta:
        model = Credential
        fields = ['credential_value']
        widgets = {
            'credential_value': forms.TextInput(attrs={'placeholder': 'Enter your credential value'}),
        }
