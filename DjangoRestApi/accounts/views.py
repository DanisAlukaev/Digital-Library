from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.http.response import JsonResponse
from accounts.models import User


@api_view(['GET', ])
def create_token(request):
    # Creates token session.

    # GET request.
    if request.method == 'GET':
        # Get id of a user from request parameters.
        user_id = request.query_params.get('id', None)
        # Check whether parameter is passed.
        if user_id is not None:
            # Get a user entity.
            user = User.objects.get(pk=user_id)
            # Check whether user with such an id exists.
            if not Token.objects.filter(user=user).exists():
                # Create token session.
                token = Token.objects.create(user=user)
                # Return JSON with token.
                return JsonResponse({'auth_token': str(token)}, safe=False)
    # If some conditions are not satisfied, then return a message.
    return JsonResponse({'message': 'Cannot create a token'}, status=status.HTTP_204_NO_CONTENT)
