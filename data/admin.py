from django.contrib import admin
from .models import Data

# Register your models here.
class dataAdmin(admin.ModelAdmin):
    list_display = ['end_year','end_year','start_year','country','title']

    

    list_per_page =50





admin.site.register(Data,dataAdmin)


