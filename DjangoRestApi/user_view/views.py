from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from storage.models import Upload
from thematic_pages.models import ThematicPage
from storage.serializers import UploadSerializer
from thematic_pages.serializers import ThematicPageSerializer
from rest_framework.decorators import api_view

"""
Available requests:
Methods	    Urls                                Actions
GET         /api/user_view/thematic_pages_list   get ThematicPages to view
GET         /api/user_view/thematic_page/:id     get Upload items to view for Thematic Page with defined id     
"""


@api_view(['GET'])
def thematic_pages_list(request):
    # get available pages
    thematic_pages = request.user.can_view

    if request.method == 'GET':
        # serialize pages
        thematic_page_serializer = ThematicPageSerializer(thematic_pages, many=True)
        # return serialized page
        return JsonResponse(thematic_page_serializer.data, safe=False)


@api_view(['GET'])
def thematic_page(request, pk):
    # Get page
    try:
        page = ThematicPage.objects.get(pk=pk)
    except Upload.DoesNotExist:
        return JsonResponse({'message': 'The page does not exist'}, status=status.HTTP_404_NOT_FOUND)

    upload = page.upload_set.filter(status=1)

    # GET request
    if request.method == 'GET':
        if page in request.user.can_view:
            # Serialize specified upload
            upload_serializer = UploadSerializer(upload, many=True)
            # Return serialized upload
            return JsonResponse(upload_serializer.data, safe=False)
        else:
            return JsonResponse({'message': "User can't view this page"}, status=status.HTTP_403_FORBIDDEN)
