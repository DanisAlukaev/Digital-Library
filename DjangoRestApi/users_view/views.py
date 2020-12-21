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
Methods	    Urls                                                Actions

views.thematic_pages_list
GET         /api/user_view/thematic_pages_list                  get ThematicPages to view

views.not_available_pages_list
GET         /api/user_view/not_available_pages_list             get ThematicPages that are not available

views.thematic_page_uploads
GET         /api/user_view/thematic_page_uploads/:pk            get Upload items to view for Thematic Page with defined id

views.request_read_rights
GET         /api/user_view/request_read_rights/:pk              request an access to Thematic Page 

views.add_to_bookmark
POST        /api/user_view/bookmark/:bookmark_pk/:upload_pk     add Upload to Bookmark Page

views.add_bookmark     
POST        /api/user_view/bookmark/add/:page_title             add new Bookmark Page
            
views.bookmarks_list 
GET         /api/user_view/bookmark_list                        get Bookmark Pages for user

views.bookmark_uploads
GET         /api/user_view/bookmark_uploads/:pk                 get Uploads of Bookmark Page
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
    # Operates on all uploads of thematic pages.

    # User should be logged in.
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)

    # Get thematic page.
    try:
        page = ThematicPage.objects.get(pk=pk)
    except ThematicPage.DoesNotExist:
        return JsonResponse({'message': 'The page does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Get all published uploads.
    upload = page.upload_set.filter(status=1)

    # GET request.
    if request.method == 'GET':
        # Check whether user follows specified page.
        if page in request.user.can_view.all():
            # Serialize uploads.
            upload_serializer = UploadSerializer(upload, many=True)
            # Return serialized upload
            return JsonResponse(upload_serializer.data, safe=False)
        else:
            # Notify that user does not follow this page.
            return JsonResponse({'message': "User can't view this page"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
def not_available_pages_list(request):
    # Operates on all available thematic pages.

    # User should be logged in.
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)
    # GET request.
    if request.method == 'GET':
        # Get all thematic pages.
        pages = ThematicPage.objects.all()
        # Exclude not available thematic pages.
        for pk_ in request.user.can_view.values('pk'):
            pk_ = pk_['pk']
            pages = pages.exclude(pk=pk_)
        # Serialize thematic pages.
        pages_serializer = ThematicPageSerializer(pages, many=True)
        # Return serialized pages.
        return JsonResponse(pages_serializer.data, safe=False)


@api_view(['GET'])
def request_read_rights(request, pk):
    # Follow thematic page.

    # User should be logged in.
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)

    # Get thematic page.
    try:
        page = ThematicPage.objects.get(pk=pk)
    except ThematicPage.DoesNotExist:
        return JsonResponse({'message': 'The page does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET request.
    if request.method == "GET":
        # Send a joining request.
        request.user.requested_pages.add(page)
        return JsonResponse({'message': 'Request sent!'})


@api_view(['GET'])
def bookmarks_list(request):
    # Get bookmark list.

    # User should be logged in.
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)

    # GET request.
    if request.method == "GET":
        # Serialize bookmark pages.
        page_serializer = BookmarkPageSerializer(request.user.bookmarkpage_set, many=True)
        # Return serialized bookmark pages.
        return JsonResponse(page_serializer.data, safe=False)


@api_view(['POST'])
def add_bookmark(request, page_title):
    # Add bookmark to a bookmark page.

    # User should be logged in.
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)

    # POST request.
    if request.method == "POST":
        # Create new instance in bookmark page.
        new_bookmark = request.user.bookmarkpage_set.create(title=page_title)
        # Serialize bookmark page.
        page_serializer = BookmarkPageSerializer(new_bookmark)
        # Return serialized bookmark page.
        return JsonResponse(page_serializer.data)


@api_view(['POST'])
def add_to_bookmark(request, bookmark_pk, upload_pk):
    # Add upload to a bookmark page.

    # User should be logged in.
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)

    # Get bookmark page.
    try:
        page = BookmarkPage.objects.get(pk=bookmark_pk)
    except BookmarkPage.DoesNotExist:
        return JsonResponse({'message': 'The Bookmark Page does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Get upload.
    try:
        upload = Upload.objects.get(pk=upload_pk)
    except Upload.DoesNotExist:
        return JsonResponse({'message': 'The upload does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # POST request.
    if request.method == "POST":
        # Upload should not violate access rights.
        if upload.status == 1 and page in request.user.bookmarkpage_set.all() and \
                upload.thematic_page in request.user.can_view.all():
            page.uploads.add(upload)
            # Serialize bookmark page.
            page_serializer = BookmarkPageSerializer(page)
            # Return serialized bookmark page.
            return JsonResponse(page_serializer.data)
        # Notify that user has no access.
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
def bookmark_uploads(request, pk):
    # Get all uploads in bookmark page.

    # User should be logged in.
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)

    # Get bookmark page.
    try:
        page = BookmarkPage.objects.get(pk=pk)
    except BookmarkPage.DoesNotExist:
        return JsonResponse({'message': 'The Bookmark Page does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Check whether user owns this bookmark page.
        if page in request.user.bookmarkpage_set.all():
            # Serialize uploads.
            upload_serializer = UploadSerializer(page.uploads, many=True)
            # Return serialized uploads.
            return JsonResponse(upload_serializer.data, safe=False)
        else:
            # Notify that user has no access.
            return JsonResponse({'message': "User can't view this page"}, status=status.HTTP_403_FORBIDDEN)
