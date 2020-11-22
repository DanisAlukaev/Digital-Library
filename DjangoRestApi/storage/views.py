from django.shortcuts import render

from django.http.response import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from accounts.models import User
from storage.models import Upload, Tag, Comment
from storage.serializers import UploadSerializer, TagSerializer, CommentSerializer
from rest_framework.decorators import api_view

"""
Available requests:
Methods	    Urls                                    Actions

views.upload_list
GET         api/uploads                             get all uploads
POST        api/uploads                             add new upload
DELETE      api/uploads                             remove all uploads
GET         api/uploads?title=[kw]                  find all uploads which title contains 'kw'
GET         api/uploads?tags=[kw]                   find all uploads with tags specified in 'kw'
GET         api/uploads?title=[kw1]&tags=[kw2]      find all uploads which title contains 'kw1' and with tags specified 
                                                    in 'kw2'

views.upload_detail
GET         api/uploads/:id                         get upload by id
PUT         api/uploads/:id                         update upload by id
DELETE      api/uploads/:id                         remove upload by id

views.upload_status
GET         api/uploads/status                      find all published uploads

views.user_contributions
GET         api/uploads/last/(?P<pk>[0-9]+)/        get three last contributions

views.tag_list
GET         api/tags                                get all tags

views.upload_comments
GET         api/uploads/comments/:id/               get all comments for upload by its id

views.comment_list
GET         api/comments/                           get all comments in a system
POST        api/comments/                           add new comments for upload

views.comment_detail
GET         api/comments/:id/                       get comments for upload by its id
PUT         api/comments/:id/                       update comment by id
DELETE      api/comments/:id/                       remove comment by id

"""


@api_view(['GET', 'POST', 'DELETE'])
def upload_list(request):
    # Operates on all uploads.
    # Allows to get details about all uploads, and create new instances of them and delete.

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
    # Operates on upload with a specified key.
    # Allows to get details about upload, modify it and delete.

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


@api_view(['GET'])
def upload_comments(request, pk):
    # Operates on all comments of a specified upload.

    # Get upload specified by a primary key.
    try:
        upload = Upload.objects.get(pk=pk)
    except Upload.DoesNotExist:
        return JsonResponse({'message': 'The upload does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET request.
    if request.method == 'GET':
        comments = Comment.objects.filter(upload=upload)
        # Serialize specified upload.
        serializer = CommentSerializer(comments, many=True)
        # Return serialized upload.
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def user_contributions(request, pk):
    # Operates on all uploads of a specified user.

    # Get upload specified by a primary key.
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The upload does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET request.
    if request.method == 'GET':
        uploads = Upload.objects.filter(user=user)[:3]
        # Serialize specified upload.
        upload_serializer = UploadSerializer(uploads, many=True)
        # Return serialized upload.
        return JsonResponse(upload_serializer.data, safe=False)


@api_view(['GET', 'PUT'])
def upload_status(request):
    # Operates on all uploads that were approved by moderators.

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
    # Operates on all tags.
    # Allows to get details about all comments.
    # Note that creation is done directly in admin panel.

    # GET request.
    if request.method == 'GET':
        # Retrieve all entries from database.
        tags = Tag.objects.all()
        # Serialize tags.
        tags_serializer = TagSerializer(tags, many=True)
        # Return serialized instances ('safe=False' for objects serialization).
        return JsonResponse(tags_serializer.data, safe=False)


@api_view(['GET', 'POST'])
def comment_list(request):
    # Operates on all comments.
    # Allows to get details about all comments, and create new instances of them.

    if request.user.is_anonymous:
        # Only for authorized users.
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)

    # GET request.
    if request.method == 'GET':
        # Retrieve all comments.
        comments = Comment.objects.all()
        # Serialize comments.
        serializer = CommentSerializer(comments, many=True)
        # Return serialized instances ('safe=False' for objects serialization).
        return JsonResponse(serializer.data, safe=False)

    # POST request.
    elif request.method == 'POST':
        # Deserialize from JSON.
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            # Save new instance.
            serializer.save(user=request.user)
            # Notify that the creation was successful.
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        # Notify that the creation was not successful :(
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, pk):
    # Operates on comment with a specified key.
    # Allows to get details about comment, modify it and delete.

    if request.user.is_anonymous:
        # Only for authorized users.
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return HttpResponse(status=404)

    # GET request.
    if request.method == 'GET':
        # Serialize comments.
        serializer = CommentSerializer(comment)
        # Return serialized instances ('safe=False' for objects serialization).
        return JsonResponse(serializer.data)

    # PUT request.
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        # Serialize comments.
        serializer = CommentSerializer(comment, data=data)
        if serializer.is_valid():
            # Update data of comment.
            serializer.save(user=request.user)
            # Return new data.
            return JsonResponse(serializer.data)
        # Something was wrong :(
        return JsonResponse(serializer.errors, status=400)

    # DELETE request.
    elif request.method == 'DELETE':
        # Delete specified comment.
        comment.delete()
        # Notify that the removal was successful.
        return JsonResponse({'message': 'Comment was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
