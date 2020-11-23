from django.http.response import JsonResponse
from rest_framework import status

from storage.models import Upload
from thematic_pages.models import ThematicPage
from storage.serializers import UploadSerializer
from thematic_pages.serializers import ThematicPageSerializer
from accounts.models import User
from accounts.serializers import UserCreateSerializer
from rest_framework.decorators import api_view

"""
Available requests:
Methods	    Urls                                                        Actions

views.moderate_page
GET         /api/moderate/thematic_page/:pk                             get uploads to moderate for a thematic page with 
                                                                        specified id

views.approve_upload
GET         /api/moderate/upload/:pk/approve                            approve upload with specified id

views.reject_upload
GET         /api/moderate/upload/:pk/reject                             reject upload with specified id

views.moderate_pages_list
GET         /api/moderate/thematic_pages_list                           get thematic pages to moderate

views.user_with_no_access_list
GET         /api/moderate/thematic_page/:pk/user_with_no_access_list    get users without access to thematic page
                        
views.user_with_access_list
GET         /api/moderate/thematic_page/:pk/user_with_access_list       get users with access to thematic page
               
views.users_requesting_access
GET         /api/moderate/thematic_page/:pk/requests                    get users requesting access to thematic page

views.add_user
POST        /api/moderate/add_user/:page_pk/:user_pk                    add user that can access thematic page                     
"""


@api_view(['GET'])
def moderate_pages_list(request):
    # Operates on all thematic pages.

    # User should be logged in.
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)

    # Get all pages available for moderating.
    thematic_pages = request.user.can_moderate

    # GET request.
    if request.method == 'GET':
        # Serialize thematic pages.
        thematic_page_serializer = ThematicPageSerializer(thematic_pages, many=True)
        # Return serialized pages.
        return JsonResponse(thematic_page_serializer.data, safe=False)


@api_view(['GET'])
def moderate_page(request, pk):
    # Operates on all pending uploads.

    # User should be logged in.
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)

    # Get page for moderating.
    try:
        page = ThematicPage.objects.get(pk=pk)
    except ThematicPage.DoesNotExist:
        return JsonResponse({'message': 'The page does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Get all pending uploads.
    upload = page.upload_set.filter(status=2)

    # GET request.
    if request.method == 'GET':
        # Check whether user is moderator of a specified page.
        if page in request.user.can_moderate.all():
            # Serialize uploads.
            upload_serializer = UploadSerializer(upload, many=True)
            # Return pending uploads.
            return JsonResponse(upload_serializer.data, safe=False)
        else:
            # Notify that user cannot moderate on this page.
            return JsonResponse({'message': "User can't moderate this page"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
def approve_upload(request, pk):
    # Approve request for uploading.

    # User should be logged in.
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)

    # Get upload specified by a primary key.
    try:
        upload = Upload.objects.get(pk=pk)
    except Upload.DoesNotExist:
        return JsonResponse({'message': 'The upload does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET request.
    if request.method == 'GET':
        # Check whether user is moderator of a specified page.
        if upload.thematic_page in request.user.can_moderate.all():
            # Approve upload.
            upload.status = 1
            # Notify that item is now approved and added.
            return JsonResponse({'message': 'The upload is now approved!'})
        else:
            # Notify that user cannot moderate on this page.
            return JsonResponse({'message': "User can't moderate this upload"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
def reject_upload(request, pk):
    # Reject request for uploading.

    # User should be logged in.
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)

    # Get upload specified by a primary key.
    try:
        upload = Upload.objects.get(pk=pk)
    except Upload.DoesNotExist:
        return JsonResponse({'message': 'The upload does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET request.
    if request.method == 'GET':
        # Check whether user is moderator of a specified page.
        if upload.thematic_page in request.user.can_moderate.all():
            # Remove upload.
            upload.delete()
            # Notify that item is now rejected and deleted.
            return JsonResponse({'message': 'Upload rejected and deleted!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            # Notify that user cannot moderate on this page.
            return JsonResponse({'message': "User can't moderate this upload"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
def user_with_access_list(request, pk):
    # Operates on users who has an access to a thematic page.

    # User should be logged in.
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)

    # Get page specified by a primary key.
    try:
        page = ThematicPage.objects.get(pk=pk)
    except ThematicPage.DoesNotExist:
        return JsonResponse({'message': 'The Thematic Page does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET request.
    if request.method == 'GET':
        # Check whether user is moderator of a specified page.
        if page in request.user.can_moderate.all():
            # Serialize an user.
            user_serializer = UserCreateSerializer(page.users, many=True)
            # Return serialized user.
            return JsonResponse(user_serializer.data, safe=False)
        else:
            # Notify that action is forbidden.
            return JsonResponse({'message': "User can't moderate this page"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
def user_with_no_access_list(request, pk):
    # Operates on users who doesn't have an access to a thematic page.

    # User should be logged in.
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)

    # Get page specified by a primary key.
    try:
        page = ThematicPage.objects.get(pk=pk)
    except ThematicPage.DoesNotExist:
        return JsonResponse({'message': 'The Thematic Page does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET request.
    if request.method == 'GET':
        if page in request.user.can_moderate.all():
            # Get all users.
            users = User.objects.all()
            # Exclude users that have access.
            for pk_ in page.users.values('pk'):
                pk_ = pk_['pk']
                users = users.exclude(pk=pk_)
            # Serialize an user.
            user_serializer = UserCreateSerializer(users, many=True)
            # Return serialized user.
            return JsonResponse(user_serializer.data, safe=False)
        else:
            # Notify that action is forbidden.
            return JsonResponse({'message': "User can't moderate this page"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
def users_requesting_access(request, pk):
    # Operates on users who request joining to a page.

    # User should be logged in.
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)

    # Get user specified by a primary key.
    try:
        page = ThematicPage.objects.get(pk=pk)
    except ThematicPage.DoesNotExist:
        return JsonResponse({'message': 'The Thematic Page does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET request.
    if request.method == 'GET':
        # Check whether user is moderator of a specified page.
        if page in request.user.can_moderate.all():
            # Serialize an user.
            user_serializer = UserCreateSerializer(page.requested_by, many=True)
            # Return serialized user.
            return JsonResponse(user_serializer.data, safe=False)
        else:
            # Notify that action is forbidden.
            return JsonResponse({'message': "User can't moderate this page"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def add_user(request, page_pk, user_pk):
    # Accept request for joining of a user.

    # User should be logged in.
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)

    # Get page specified by a primary key.
    try:
        page = ThematicPage.objects.get(pk=page_pk)
    except ThematicPage.DoesNotExist:
        return JsonResponse({'message': 'The Thematic Page does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Get user specified by a primary key.
    try:
        user = User.objects.get(pk=user_pk)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # POST request.
    if request.method == 'POST':
        # Check whether user is moderator of a specified page.
        if page in request.user.can_moderate.all():
            # Remove request.
            user.requested_pages.remove(page)
            # Add new follower.
            page.users.add(user)
            # Serialize an user.
            user_serializer = UserCreateSerializer(user)
            # Return serialized user.
            return JsonResponse(user_serializer.data)
        else:
            return JsonResponse({'message': "User can't moderate this page"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def decline_user(request, page_pk, user_pk):
    # Decline request for joining of a user.

    # User should be logged in.
    if request.user.is_anonymous:
        return JsonResponse({'message': "No access"}, status=status.HTTP_403_FORBIDDEN)

    # Get page specified by a primary key.
    try:
        page = ThematicPage.objects.get(pk=page_pk)
    except ThematicPage.DoesNotExist:
        return JsonResponse({'message': 'The Thematic Page does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Get user specified by a primary key.
    try:
        user = User.objects.get(pk=user_pk)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # POST request.
    if request.method == 'POST':
        # Check whether user is moderator of a specified page.
        if page in request.user.can_moderate.all():
            # Remove request.
            user.requested_pages.remove(page)
            # Return notification.
            return JsonResponse({'message': "User was declined."})
        else:
            # Notify that action is forbidden.
            return JsonResponse({'message': "User can't moderate this page"}, status=status.HTTP_403_FORBIDDEN)
