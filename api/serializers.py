from rest_framework import serializers
from data.models import Data



class Data_serializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'