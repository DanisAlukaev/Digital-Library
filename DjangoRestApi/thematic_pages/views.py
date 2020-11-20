from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from thematic_pages.models import ThematicPage
from thematic_pages.serializers import ThematicPageSerializer
from rest_framework.decorators import api_view

"""
Available requests:
Methods	    Urls                          Actions
GET         api/thematic_pages             get all thematic_pages
GET         api/thematic_pages/:id         get Thematic Pages by id
POST        api/thematic_pages             add new ThematicPage
PUT         api/thematic_pages/:id         update Thematic Page by id
DELETE      api/thematic_pages             remove all thematic_pages
DELETE      api/thematic_pages/:id         remove all Uploads of Thematic Page and the Page itself by id
"""


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
    # Get Thematic Page  specified by a primary key
    try:
        page = ThematicPage.objects.get(pk=pk)
    except ThematicPage.DoesNotExist:
        return JsonResponse({'message': 'The page does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET request
    if request.method == 'GET':
        # Serialize specified ThematicPage
        thematic_page_serializer = ThematicPageSerializer(page)
        # Return serialized Thematic Page
        return JsonResponse(thematic_page_serializer.data)

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
        # Delete Thematic Page
        page.delete()
        # Notify that the removal was successful
        return JsonResponse({'message': 'Thematic Page was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)