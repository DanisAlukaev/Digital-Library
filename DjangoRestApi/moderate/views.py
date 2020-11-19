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
GET         /api/moderate/thematic_page/:id     get Upload items to moderate for Thematic Page with defined id     
PUT         /api/moderate/upload/:id/approve    approve upload with given id
PUT         /api/moderate/upload/:id/reject     reject upload with given id
GET         /api/moderate/thematic_pages_list   get ThematicPages to moderate
"""


@api_view(['GET'])
def moderate_pages_list(request):
    # get pages available for moderating to user
    thematic_pages = request.user.can_moderate

    if request.method == 'GET':
        # serialize pages
        thematic_page_serializer = ThematicPageSerializer(thematic_pages, many=True)
        # return serialized page
        return JsonResponse(thematic_page_serializer.data, safe=False)


@api_view(['GET'])
def moderate_page(request, pk):
    # Get page for moderating
    try:
        page = ThematicPage.objects.get(pk=pk)
    except Upload.DoesNotExist:
        return JsonResponse({'message': 'The page does not exist'}, status=status.HTTP_404_NOT_FOUND)

    upload = page.upload_set.filter(status=2)

    # GET request
    if request.method == 'GET':
        if page in request.user.can_moderate:
            # Serialize specified upload
            upload_serializer = UploadSerializer(upload, many=True)
            # Return serialized upload
            return JsonResponse(upload_serializer.data, safe=False)
        else:
            return JsonResponse({'message': "User can't moderate this page"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['PUT'])
def approve_upload(request, pk):
    # Get upload specified by a primary key
    try:
        upload = Upload.objects.get(pk=pk)
    except Upload.DoesNotExist:
        return JsonResponse({'message': 'The upload does not exist'}, status=status.HTTP_404_NOT_FOUND)
    # PUT request
    if request.method == 'PUT':
        if upload.thematic_page in request.user.can_moderate:
            upload.status = 1
            # Return data with status = 1
            return JsonResponse({'message': 'The upload is now approved!'})
        else:
            return JsonResponse({'message': "User can't moderate this upload"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['PUT'])
def reject_upload(request, pk):
    # Get upload specified by a primary key
    try:
        upload = Upload.objects.get(pk=pk)
    except Upload.DoesNotExist:
        return JsonResponse({'message': 'The upload does not exist'}, status=status.HTTP_404_NOT_FOUND)
    # PUT request
    if request.method == 'PUT':
        if upload.thematic_page in request.user.can_moderate:
            # delete upload
            upload.delete()
            # Notify that item is now rejected and deleted
            return JsonResponse({'message': 'Upload rejected and deleted!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message': "User can't moderate this upload"}, status=status.HTTP_403_FORBIDDEN)
