from django.db.models import fields
from rest_framework import serializers
from .models import Item
 
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('username','name','brand', 'modal', 'category', 'year','mindistance','maxdistance','installment','distance','img', 'transmissionType', 'bodyType', 'price', 'condition', 'paymentoption','created','updated')

