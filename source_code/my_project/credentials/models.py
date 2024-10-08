from django.db import models
from django.contrib.auth.models import User

class Credential(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="credentials")
    credential_value = models.TextField()  # Credential value (e.g., password, API key)
    created_at = models.DateTimeField(auto_now_add=True)  # Credential creation timestamp
    
    class Meta:
        unique_together = ('user', 'credential_value')  # Ensure unique credentials per user

    def __str__(self):
        return f'Credential for {self.user.username} (Added on {self.credential_value})'
