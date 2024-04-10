from django.shortcuts import render
from .models import Data
from django.http import JsonResponse
from django.db.models import Avg,Count


# Create your views here.


def dashboard(request):
    Datatable = Data.objects.all()
    data_count=Datatable.count()
    #country count
    country_query=Data.objects.values('country').annotate(dcount=Count('country')).order_by('-dcount')[1:11]
    country_count=country_query.count()

    #region count
    region_query=Data.objects.values('region').annotate(dcount=Count('region')).order_by('-dcount')[1:]
    region_count=region_query.count()

    #topic
    topic_query=Data.objects.values('topic').annotate(dcount=Count('topic')).order_by('-dcount')[1:11]
    topic_count=topic_query.count()
    context ={
       
        'Datatable':Datatable,
        'country_query':country_query,
        'country_count':country_count,
        'region_count':region_count,
        'topic_count':topic_count,
        'data_count':data_count,
        'topic_query':topic_query,

       

    }
    
    return render(request,"base/index.html",context)


def table_page(request):
   Datatable = Data.objects.all()
   context={
      'Datatable':Datatable

   }
   return render(request,"base/datatable.html",context)





def chart_data(request):
    int_lables=[]
    int_data=[]
    year=[]
    yr_count=[]
    region=[]
    likelihood=[]
    topic=[]
    count_topic=[]
    rel_country=[]
    relevance=[]


    Avgintensity= Data.objects.values('country').annotate(Avg('intensity')).order_by('-country')[1:9]
    Year_count =Data.objects.values('end_year').annotate(dcount=Count('end_year'))[1:18]
    Avglikelihood= Data.objects.values('region').annotate(Avg('likelihood'))[1:31]
    topic_count=Data.objects.values('topic').annotate(dcount=Count('pk')).order_by('-dcount')[1:31]
    Avgrelevance= Data.objects.values('country').annotate(Avg('relevance')).order_by('-relevance__avg')[1:11]



    for data in Avgintensity:
       int_lables.append(data['country'])
       int_data.append(data['intensity__avg'])

    for data in Year_count:
       year.append(data['end_year'])
       yr_count.append(data['dcount'])

    for data in Avglikelihood:
       region.append(data['region'])
       likelihood.append(data['likelihood__avg'])



    for data in topic_count:
       topic.append(data['topic'])
       count_topic.append(data['dcount'])

    
    for data in Avgrelevance:
       rel_country.append(data['country'])
       relevance.append(data['relevance__avg'])
       data={
        'int_lables': int_lables,
        'int_data': int_data,
        'year':year,
        'yr_count':yr_count,
        'region':region,
        'likelihood':likelihood,
        'topic':topic,
        'count_topic':count_topic,
        'rel_country':rel_country,
        'relevance':relevance

    }
    return JsonResponse(data)





