from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request, *args, **kwargs):
    """
    Demonstration of an approach to restrict accessing of routes.
    Correspondent route is available only for logged-in users.
    """
    return Response(data="Only for Logged in User", status=status.HTTP_200_OK)
