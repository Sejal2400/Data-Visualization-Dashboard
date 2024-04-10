from rest_framework import generics
from rest_framework.response import Response
from data.models import Data
from .serializers import Data_serializer



class List_data(generics.ListAPIView):
    queryset = Data.objects.all()
    serializer_class = Data_serializer
    
    