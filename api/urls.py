from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    #endpoint to list all the data
    path('list_data/',views.List_data.as_view(),name='List_data'),
   
   
    
]