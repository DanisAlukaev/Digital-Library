from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from storage.models import Upload, BookmarkPage
from thematic_pages.models import ThematicPage
from storage.serializers import UploadSerializer, BookmarkPageSerializer
from thematic_pages.serializers import ThematicPageSerializer
from rest_framework.decorators import api_view

"""
Available requests:
Methods	    Urls                                         Actions

views.thematic_pages_list
GET         /api/user_view/thematic_pages_list           get ThematicPages to view

GET         /api/user_view/not_available_pages_list      get ThematicPages that are not available

GET         /api/user_view/thematic_page_uploads/:pk     get Upload items to view for Thematic Page with defined id

GET         /api/user_view/request_read_rights/:pk       request an access to Thematic Page 

POST         /api/user_view/bookmark/                    Add Upload to Bookmark Page

            :bookmark_pk/:upload_pk
POST        /api/user_view/bookmark/add/                 Add new Bookmark Page
            :page_title
            
GET         /api/user_view/bookmark_list                 Get Bookmark Pages for user

GET         /api/user_view/bookmark_uploads/:pk          Get Uploads of Bookmark Page
"""


@api_view(['GET'])
def thematic_pages_list(request):
    # Operates on all thematic pages.

    # User should be logged in.
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)

    # Get all available pages.
    thematic_pages = request.user.can_view

    # GET request.
    if request.method == 'GET':
        # Serialize pages.
        thematic_page_serializer = ThematicPageSerializer(thematic_pages, many=True)
        # Return serialized pages.
        return JsonResponse(thematic_page_serializer.data, safe=False)


@api_view(['GET'])
def thematic_page_uploads(request, pk):
    # user should be logged in
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)
    # Get page
    try:
        page = ThematicPage.objects.get(pk=pk)
    except ThematicPage.DoesNotExist:
        return JsonResponse({'message': 'The page does not exist'}, status=status.HTTP_404_NOT_FOUND)

    upload = page.upload_set.filter(status=1)

    # GET request
    if request.method == 'GET':
        if page in request.user.can_view.all():
            # Serialize specified upload
            upload_serializer = UploadSerializer(upload, many=True)
            # Return serialized upload
            return JsonResponse(upload_serializer.data, safe=False)
        else:
            return JsonResponse({'message': "User can't view this page"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
def not_available_pages_list(request):
    # user should be logged in
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)
    # GET request
    if request.method == 'GET':
        pages = ThematicPage.objects.all()
        for pk_ in request.user.can_view.values('pk'):
            pk_ = pk_['pk']
            pages = pages.exclude(pk=pk_)
        # serialize pages
        pages_serializer = ThematicPageSerializer(pages, many=True)
        # return serialized pages
        return JsonResponse(pages_serializer.data, safe=False)


@api_view(['GET'])
def request_read_rights(request, pk):
    # user should be logged in
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)

    # Get page
    try:
        page = ThematicPage.objects.get(pk=pk)
    except ThematicPage.DoesNotExist:
        return JsonResponse({'message': 'The page does not exist'}, status=status.HTTP_404_NOT_FOUND)
    # GET request
    if request.method == "GET":
        request.user.requested_pages.add(page)
        return JsonResponse({'message': 'Request sent!'})


@api_view(['GET'])
def bookmarks_list(request):
    # user should be logged in
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)
    if request.method == "GET":
        # serialize Bookmark Pages
        page_serializer = BookmarkPageSerializer(request.user.bookmarkpage_set, many=True)
        # return serialized Bookmark Pages
        return JsonResponse(page_serializer.data, safe=False)


@api_view(['POST'])
def add_bookmark(request, page_title):
    # user should be logged in
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)
    if request.method == "POST":
        new_bookmark = request.user.bookmarkpage_set.create(title=page_title)
        # serialize Bookmark Page
        page_serializer = BookmarkPageSerializer(new_bookmark)
        # return serialized Bookmark Page
        return JsonResponse(page_serializer.data)


@api_view(['POST'])
def add_to_bookmark(request, bookmark_pk, upload_pk):
    # user should be logged in
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)
    # Get bookmark page specified by a primary key
    try:
        page = BookmarkPage.objects.get(pk=bookmark_pk)
    except BookmarkPage.DoesNotExist:
        return JsonResponse({'message': 'The Bookmark Page does not exist'}, status=status.HTTP_404_NOT_FOUND)
    # Get upload specified by a primary key
    try:
        upload = Upload.objects.get(pk=upload_pk)
    except Upload.DoesNotExist:
        return JsonResponse({'message': 'The upload does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "POST":
        if upload.status == 1 and page in request.user.bookmarkpage_set.all() and \
                upload.thematic_page in request.user.can_view.all():
            page.uploads.add(upload)
            # serialize Bookmark Page
            page_serializer = BookmarkPageSerializer(page)
            # return serialized Bookmark Page
            return JsonResponse(page_serializer.data)
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
def bookmark_uploads(request, pk):
    # user should be logged in
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)
    # Get bookmark page specified by a primary key
    try:
        page = BookmarkPage.objects.get(pk=pk)
    except BookmarkPage.DoesNotExist:
        return JsonResponse({'message': 'The Bookmark Page does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        if page in request.user.bookmarkpage_set.all():
            # Serialize uploads
            upload_serializer = UploadSerializer(page.uploads, many=True)
            # Return serialized upload
            return JsonResponse(upload_serializer.data, safe=False)
        else:
            return JsonResponse({'message': "User can't view this page"}, status=status.HTTP_403_FORBIDDEN)
