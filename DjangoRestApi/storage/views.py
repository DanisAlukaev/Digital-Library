from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from storage.models import Upload, Tag
from storage.serializers import UploadSerializer, TagSerializer
from rest_framework.decorators import api_view

"""
Available requests:
Methods	    Urls                                    Actions
GET         api/uploads                             get all Uploads
GET         api/uploads/:id                         get Uploads by id
POST        api/uploads                             add new Uploads
PUT         api/uploads/:id                         update Uploads by id
DELETE      api/uploads/:id                         remove Uploads by id
DELETE      api/uploads                             remove all Uploads
GET         api/uploads/status                      find all published Uploads
GET         api/uploads?title=[kw]                  find all Uploads which title contains 'kw'
GET         api/uploads?tags=[kw]                   find all Uploads with tags specified in 'kw'
GET         api/uploads?title=[kw1]&tags=[kw2]      find all Uploads which title contains 'kw1' and with tags specified 
                                                    in 'kw2'
GET         api/tags                                get all tags
"""


@api_view(['GET', 'POST', 'DELETE'])
def upload_list(request):
    # GET request.
    if request.method == 'GET':
        # Retrieve all entries from database.
        uploads = Upload.objects.all()

        # Check whether request had title parameter.
        title = request.query_params.get('title', None)
        if title is not None:
            # If so, then find uploads with specified title.
            uploads = uploads.filter(title__icontains=title)

        # Check whether request had tags parameter.
        tags = request.query_params.get('tags', None)
        if tags is not None:
            # Get ids of tags.
            ids = [int(id) for id in tags.split(',')]
            # Find uploads with specified tags.
            uploads = uploads.filter(tags__in=ids).distinct()

        # Serialize uploads.
        uploads_serializer = UploadSerializer(uploads, many=True)
        # Return serialized instances ('safe=False' for objects serialization).
        return JsonResponse(uploads_serializer.data, safe=False)

    # POST request
    elif request.method == 'POST':
        # Deserialize from JSON.
        upload_serializer = UploadSerializer(data=request.data)
        if upload_serializer.is_valid():
            # Save new instance.
            upload_serializer.save(user=request.user)
            # Notify that the creation was successful.
            return JsonResponse(upload_serializer.data, status=status.HTTP_201_CREATED)
        # Notify that the creation was not successful :(
        return JsonResponse(upload_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE request
    elif request.method == 'DELETE':
        # Delete all entries from database.
        count = Upload.objects.all().delete()
        # Notify that the removal was successful.
        return JsonResponse({'message': '{} Uploads were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def upload_detail(request, pk):
    # Get upload specified by a primary key.
    try:
        upload = Upload.objects.get(pk=pk)
    except Upload.DoesNotExist:
        return JsonResponse({'message': 'The upload does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET request.
    if request.method == 'GET':
        # Serialize specified upload.
        upload_serializer = UploadSerializer(upload)
        # Return serialized upload.
        return JsonResponse(upload_serializer.data)

    # PUT request.
    elif request.method == 'PUT':
        # Deserialize from JSON.
        upload_serializer = UploadSerializer(upload, data=request.data)
        if upload_serializer.is_valid():
            # Update data of upload.
            upload_serializer.save(user=request.user)
            # Return new data.
            return JsonResponse(upload_serializer.data)
        # Something was wrong :(
        return JsonResponse(upload_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE request
    elif request.method == 'DELETE':
        # Delete specified upload.
        upload.delete()
        # Notify that the removal was successful.
        return JsonResponse({'message': 'Upload was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT'])
def upload_status(request):
    # Retrieve all published uploads from database.
    uploads = Upload.objects.filter(status=1)

    # GET request.
    if request.method == 'GET':
        # Serialize published uploads.
        uploads_serializer = UploadSerializer(uploads, many=True)
        # Return serialized instances.
        return JsonResponse(uploads_serializer.data, safe=False)


@api_view(['GET'])
def tag_list(request):
    # GET request.
    if request.method == 'GET':
        # Retrieve all entries from database.
        tags = Tag.objects.all()
        # Serialize tags.
        tags_serializer = TagSerializer(tags, many=True)
        # Return serialized instances ('safe=False' for objects serialization).
        return JsonResponse(tags_serializer.data, safe=False)
