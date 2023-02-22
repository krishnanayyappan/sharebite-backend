from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Section, Item, Modifier, Mapping
from .serializer import SectionSerializer, ItemSerializer, ModifierSerializer, MappingSerializer, MenuSerializer
from rest_framework import serializers
from rest_framework import status


@api_view(['GET'])
def view_menu(request):
    if request.query_params:
        menus = Section.objects.filter(**request.query_params.dict())
    else:
        menus = Section.objects.all()

    # if there is something in items else raise error
    if menus:
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_sections(request):
    section = SectionSerializer(data=request.data)

    # validating if section already exists
    if Section.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Section already exists')

    if section.is_valid():
        section.save()
        return Response(section.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_sections(request):
    # checking for the parameters from the URL
    if request.query_params:
        sections = Section.objects.filter(**request.query_params.dict())
    else:
        sections = Section.objects.all()

    # return the data in "sections" through serializer
    # return 404 error if there is no data for sections
    if sections:
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_sections(request, pk):
    # use the primary key of the section given in the URL to get the section
    # and update the DB with the value(s) entered by user
    section = Section.objects.get(pk=pk)
    data = SectionSerializer(instance=section, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_sections(request, pk):
    # use the primary key of the section given in the URL to delete the section
    # if it is not a valid primary key, return 404 error
    section = get_object_or_404(Section, pk=pk)
    section.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def add_items(request):
    # function add an item to the DB. User is expected to enter a primary key that is not present in the DB
    # else, error will be thrown
    item = ItemSerializer(data=request.data)

    # validating if item already exists
    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_items(request):
    # checking for the parameters from the URL
    if request.query_params:
        items = Item.objects.filter(**request.query_params.dict())
    else:
        items = Item.objects.all()

    # return the data in "items" through serializer
    # return 404 error if there is no data for sections
    if items:
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_items(request, pk):
    # use the primary key of the item given in the URL to get the item
    # and update the DB with the value(s) entered by user
    items = Item.objects.get(pk=pk)
    data = ItemSerializer(instance=items, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_items(request, pk):
    # use the primary key of the item given in the URL to delete the item
    # if it is not a valid primary key, return 404 error
    items = get_object_or_404(Item, pk=pk)
    items.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def add_modifiers(request):
    modifier = ModifierSerializer(data=request.data)

    # validating if modifier already exists
    if Modifier.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This modifier already exists')

    if modifier.is_valid():
        modifier.save()
        return Response(modifier.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_modifiers(request):
    # function to get all the modifiers present in the DB
    if request.query_params:
        modifiers = Modifier.objects.filter(**request.query_params.dict())
    else:
        modifiers = Modifier.objects.all()

    # return the data in "items" through serializer
    # return 404 error if there is no data for sections
    if modifiers:
        serializer = ModifierSerializer(modifiers, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_modifiers(request, pk):
    # use the primary key of the modifier given in the URL to get the modifier
    # and update the DB with the value(s) entered by user
    modifier = Modifier.objects.get(pk=pk)
    data = ModifierSerializer(instance=modifier, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_modifiers(request, pk):
    # use the primary key of the modifier given in the URL to delete the modifier
    # if it is not a valid primary key, return 404 error
    modifier = get_object_or_404(Modifier, pk=pk)
    modifier.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['PATCH'])
def map_items_and_modifiers(request, pk):
    # Map items and modifiers. Items and Modifiers have a many-to-many relationship since an Item can be
    # mapped to more than one modifier, and vice versa.
    # This function will get invoked when user hits the "mapping/add/<primary-key>" endpoint.
    # In this function, primary key in the URL is treated as modifier's primary key, and the user has to
    # enter the Items in list format. For example, {"items":[1,3]}
    # We return a 404 error if a modifier with that primary key is not found in the DB
    modifiers = Modifier.objects.get(pk=pk)
    data = ModifierSerializer(instance=modifiers, data=request.data, partial=True)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
