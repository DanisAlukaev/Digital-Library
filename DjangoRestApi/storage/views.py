from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from storage.models import Upload, Tag, ThematicPage
from storage.serializers import UploadSerializer, TagSerializer, ThematicPageSerializer
from rest_framework.decorators import api_view

"""
Available requests:
Methods	    Urls                          Actions
GET         api/uploads                   get all Uploads
GET         api/uploads/:id               get Uploads by id
POST        api/uploads                   add new Uploads
PUT         api/uploads/:id               update Uploads by id
DELETE      api/uploads/:id               remove Uploads by id
DELETE      api/uploads                   remove all Uploads


GET         api/uploads/published         find all published Uploads
GET         api/uploads?title=[kw]        find all Uploads which title contains 'kw'


GET         api/tags                      get all tags

GET         api/ThematicPages             get all ThematicPages
GET         api/ThematicPages/:page_name  get Thematic Pages by id
POST        api/ThematicPages             add new ThematicPage
PUT         api/ThematicPages/:page_name  update Thematic Page by id
DELETE      api/ThematicPages             remove all ThematicPages
DELETE      api/ThematicPages/:page_name  remove all Uploads of Thematic Page and the Page itself by id
"""


@api_view(['GET', 'POST', 'DELETE'])
def upload_list(request):
    # GET request
    if request.method == 'GET':
        # Retrieve all entries from database
        uploads = Upload.objects.all()

        # Check whether request had title parameter
        title = request.query_params.get('title', None)
        if title is not None:
            # If so, then find uploads with specified title
            uploads = uploads.filter(title__icontains=title)

        # Serialize uploads
        uploads_serializer = UploadSerializer(uploads, many=True)
        # Return serialized instances ('safe=False' for objects serialization)
        return JsonResponse(uploads_serializer.data, safe=False)

    # POST request
    elif request.method == 'POST':
        # Parse request object
        upload_data = JSONParser().parse(request)

        # Deserialize from JSON
        upload_serializer = UploadSerializer(data=upload_data)
        if upload_serializer.is_valid():
            # Save new instance
            upload_serializer.save(user=request.user)
            # Notify that the creation was successful
            return JsonResponse(upload_serializer.data, status=status.HTTP_201_CREATED)
        # Notify that the creation was not successful :(
        return JsonResponse(upload_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE request
    elif request.method == 'DELETE':
        # Delete all entries from database
        count = Upload.objects.all().delete()
        # Notify that the removal was successful
        return JsonResponse({'message': '{} Uploads were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def upload_detail(request, pk):
    # Get upload specified by a primary key
    try:
        upload = Upload.objects.get(pk=pk)
    except Upload.DoesNotExist:
        return JsonResponse({'message': 'The upload does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET request
    if request.method == 'GET':
        # Serialize specified upload
        upload_serializer = UploadSerializer(upload)
        # Return serialized upload
        return JsonResponse(upload_serializer.data)

    # PUT request
    elif request.method == 'PUT':
        # Parse request object
        upload_data = JSONParser().parse(request)
        # Deserialize from JSON
        upload_serializer = UploadSerializer(upload, data=upload_data)
        if upload_serializer.is_valid():
            # Update data of upload
            upload_serializer.save(user=request.user)
            # Return new data
            return JsonResponse(upload_serializer.data)
        # Something was wrong :(
        return JsonResponse(upload_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE request
    elif request.method == 'DELETE':
        # Delete specified upload
        upload.delete()
        # Notify that the removal was successful
        return JsonResponse({'message': 'Upload was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def upload_status(request):
    # Retrieve all published uploads from database
    uploads = Upload.objects.filter(status=1)

    # GET request
    if request.method == 'GET':
        # Serialize published uploads
        uploads_serializer = UploadSerializer(uploads, many=True)
        # Return serialized instances
        return JsonResponse(uploads_serializer.data, safe=False)


@api_view(['GET'])
def tag_list(request):
    # GET request
    if request.method == 'GET':
        # Retrieve all entries from database
        tags = Tag.objects.all()
        # Serialize tags
        tags_serializer = TagSerializer(tags, many=True)
        # Return serialized instances ('safe=False' for objects serialization)
        return JsonResponse(tags_serializer.data, safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def thematic_page_list(request):
    # GET request
    if request.method == 'GET':
        # Retrieve all entries from database
        pages = ThematicPage.objects.all()

        # Check whether request had name parameter
        name = request.query_params.get('name', None)
        if name is not None:
            # If so, then find Thematic Pages with specified title
            pages = pages.filter(name__icontains=name)

        # Serialize Thematic Pages
        thematic_pages_serializer = ThematicPageSerializer(pages, many=True)
        # Return serialized instances ('safe=False' for objects serialization)
        return JsonResponse(thematic_pages_serializer.data, safe=False)

    # POST request
    elif request.method == 'POST':
        # Parse request object
        thematic_page_data = JSONParser().parse(request)

        # Deserialize from JSON
        thematic_page_serializer = ThematicPageSerializer(data=thematic_page_data)
        if thematic_page_serializer.is_valid():
            # Save new instance
            thematic_page_serializer.save()
            # Notify that the creation was successful
            return JsonResponse(thematic_page_serializer.data, status=status.HTTP_201_CREATED)
        # Notify that the creation was not successful :(
        return JsonResponse(thematic_page_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE request
    elif request.method == 'DELETE':
        # Delete all entries from database
        count = ThematicPage.objects.all().delete()
        # Notify that the removal was successful
        return JsonResponse({'message': '{} Thematic Pages were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def thematic_page_detail(request, pk):
    # Get Thematic Page uploads specified by a primary key of the page
    try:
        page = ThematicPage.objects.get(pk=pk)
    except Upload.DoesNotExist:
        return JsonResponse({'message': 'The page does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET request
    if request.method == 'GET':
        # Serialize specified ThematicPage
        thematic_page_serializer = ThematicPageSerializer(page, many=True)
        # Return serialized Thematic Page
        return JsonResponse(thematic_page_serializer.data, safe=False)

    # PUT request
    elif request.method == 'PUT':
        # Parse request object
        thematic_page_data = JSONParser().parse(request)
        # Deserialize from JSON
        thematic_page_serializer = ThematicPageSerializer(page, data=thematic_page_data)
        if thematic_page_serializer.is_valid():
            # Update data of thematic page
            thematic_page_serializer.save()
            # Return new data
            return JsonResponse(thematic_page_serializer.data)
        # Something was wrong :(
        return JsonResponse(thematic_page_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE request
    elif request.method == 'DELETE':
        # Delete uploads of specified Thematic Page
        page.upload_set.delete()
        # Delete Thematic Page
        page.delete()
        # Notify that the removal was successful
        return JsonResponse({'message': 'Thematic Page was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
