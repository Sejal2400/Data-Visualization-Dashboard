from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('datatable/',views.table_page,name='table_page'),


    #json data  endpoint for charts.js
    path('chart_data/',views.chart_data,name='chart_data'),
   
    
]