from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from .models import Credential
from .serializers import CredentialSerializer
import logging

# Set up logging
logger = logging.getLogger(__name__)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def credential_list(request):
    if request.method == 'GET':
        # Fetch credentials for the authenticated user
        credentials = Credential.objects.filter(user=request.user)
        serializer = CredentialSerializer(credentials, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Associate the authenticated user with the new credential
        data = request.data.copy()  # Create a mutable copy of request data
        data['user'] = request.user.id  # Add the authenticated user's ID
        
        serializer = CredentialSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Save with the authenticated user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Log validation errors for debugging
            logger.error("Validation Errors: %s", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def credential_detail(request, pk):
    try:
        credential = Credential.objects.get(pk=pk, user=request.user)
    except Credential.DoesNotExist:
        return Response({'error': 'Credential not found or unauthorized access.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Retrieve the specific credential
        serializer = CredentialSerializer(credential)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # Update the specific credential
        serializer = CredentialSerializer(credential, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete the specific credential
        credential.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
