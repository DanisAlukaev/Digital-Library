from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.http.response import JsonResponse
from rest_framework import serializers
from accounts.models import User


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request, *args, **kwargs):
    """
    Demonstration of an approach to restrict accessing of routes.
    Correspondent route is available only for logged-in users.
    """
    return Response(data="Only for Logged in User", status=status.HTTP_200_OK)


@api_view(['GET', ])
def create_token(request):
    # GET request.
    if request.method == 'GET':
        user_id = request.query_params.get('id', None)
        if user_id is not None:
            user = User.objects.get(pk=user_id)
            if not Token.objects.filter(user=user).exists():
                token = Token.objects.create(user=user)
                return JsonResponse(str(token), safe=False)
    return JsonResponse({'message': 'Cannot create a token'}, status=status.HTTP_204_NO_CONTENT)
