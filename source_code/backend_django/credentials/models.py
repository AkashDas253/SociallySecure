from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()  # This loads the variables from .env into the environment

# Fetch the encryption key from the environment variable
key = os.getenv('FERMAT_KEY')

# Ensure the key is available
if not key:
    raise ValueError("FERMAT_KEY environment variable is missing.")

# Fernet encryption instance
fernet = Fernet(key)

class Credential(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="credentials")
    credential_value = models.TextField()  # The credential value (e.g., password, API key)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the credential was added

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'credential_value'], name='unique_credential')
        ]

    def __str__(self):
        return f'Credential for {self.user.username} (Added on {self.created_at})'

    # Method to encrypt the credential before saving to the database
    def encrypt_credential(self):
        """Encrypt the credential_value using Fernet encryption."""
        return fernet.encrypt(self.credential_value.encode()).decode()

    # Method to decrypt the credential when retrieving it
    def decrypt_credential(self):
        """Decrypt the credential_value when needed."""
        return fernet.decrypt(self.credential_value.encode()).decode()

    # Override the save method to encrypt the credential_value before saving to the database
    def save(self, *args, **kwargs):
        if self.credential_value:  # Ensure there is a credential_value to encrypt
            self.credential_value = self.encrypt_credential()
        super().save(*args, **kwargs)  # Call the parent save method

    # A class method to retrieve decrypted credential value
    @classmethod
    def get_decrypted_credential(cls, credential_id):
        """Retrieve the decrypted credential_value using the credential's ID."""
        try:
            credential = cls.objects.get(id=credential_id)
            return credential.decrypt_credential()
        except cls.DoesNotExist:
            raise ValueError(f"Credential with ID {credential_id} does not exist.")
