from dataclasses import field
from operator import mod
from rest_framework import serializers
from . import models
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model= models.Category
        fields=['name','description']