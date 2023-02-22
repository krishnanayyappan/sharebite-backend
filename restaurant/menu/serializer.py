from django.db.models import fields
from rest_framework import serializers
from .models import Section, Item, Modifier, Mapping


# This serializer is for CRUD operations on Section data
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'name', 'description')


# This serializer is for CRUD operations on Modifier data
class ModifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modifier
        fields = ('id', 'name', 'description', 'items')
        extra_kwargs = {'items': {'required': False}}


# This serializer is for CRUD operations on Item data
class ItemSerializer(serializers.ModelSerializer):
    modifiers = ModifierSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'price', 'sectionid', 'modifiers')
        extra_kwargs = {'modifiers': {'required': False}}


class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapping
        fields = ('id', 'mod_id', 'items_id')


# This serializer is for getting Modifier info to display the Menu JSON starting from
# Sections to Modifiers
class GetModifiersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modifier
        fields = ('id', 'name')


class GetItemsSerializer(serializers.ModelSerializer):
    modifiers = GetModifiersSerializer(many=True)

    class Meta:
        model = Item
        fields = ('id', 'name', 'modifiers')


# This serializer calls GetItemsSerializer to get the Items for the chosen Section value,
# which in turn calls GetModifiersSerializer to get the Modifiers mapped to the Items
class MenuSerializer(serializers.ModelSerializer):
    items = GetItemsSerializer(many=True)

    class Meta:
        model = Section
        fields = ('id', 'name', 'items')
