from django.shortcuts import render,get_list_or_404
from companies.models import Company,Contact,Country,ContactType,ContactResult
from .serializers import CompanySerializer,ContactSerializer,CountrySerializer,ContactResultSerializer,ContactTypeSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum,Count,Avg
# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response


from django.views.generic import ListView
from django_pandas.io import read_frame # **important to convert queryset to pandas df
from django.http import HttpResponse,response
from rest_framework.serializers import Serializer

#for testing aggrigation
import pandas as pd
from .services import Stats
from .stats_objects import *
import json



# All Companies View 
class CompanyApiCL(ListCreateAPIView):
   
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    # permission_classes = [IsAuthenticated]


class CompanyApiRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    lookup_field = "pk"
    queryset = Company.objects.all()
    
  #  permission_classes = [IsAuthenticated]


class ContactApiCL(ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
  #  permission_classes = [IsAuthenticated]


    def get_queryset(self):
        pk = self.kwargs["pk"]
        qs = get_list_or_404(Contact,company__pk = pk)
   
        return qs

class ContactApiRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    lookup_field = "pk"
    queryset = Contact.objects.all()
    
  #  permission_classes = [IsAuthenticated]

class CountryList(ListCreateAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    


class ContactResultList(ListCreateAPIView):
    serializer_class = ContactResultSerializer
    queryset = ContactResult.objects.all()


class ContactTypeList(ListCreateAPIView):
    serializer_class = ContactTypeSerializer
    queryset = ContactType.objects.all()



class MyDataFrameAPIView(APIView):
    def get(self, request):
        
        # create a df
        stats = Stats()
        CountryToConmpny = stats.get_CountryToConmpny()
       

        # create a dictionary from the analitics
        data= {
            "CountryToConmpny": CountryToConmpny
        }


        return Response(data)




    # permission_classes = [IsAuthenticated]

# class Analytics(ListView):
#     # serializer_class = AnalyticsSerialize

#     # serializer_class = ContactSerializer
    
#     def get_queryset(self):
#         qs1 = Contact.objects.all().aggregate("typ")
#         qs = Contact.objects.all()

#         print(qs1)

#         return qs
        






# class MyModelList(ListAPIView):
#     serializer_class = 

#     def get_queryset(self):
#         pandas_stats = Stats()
#         qs = pandas_stats.get_CountryToConmpny()
#         return qs


# def get_qs(request):
#     # qs = Book.objects.aggregate(Count("price"))
#     # qs = Company.objects.aaggregate(Count("company"))

#     #just one query
#     # qs = Company.objects.aggregate(Count("email"))

#     qs = Contact.objects.values('id','company_id' ,'typ_id__contact_type',  'date', 'result_id')
#     qs2 = Contact.objects.prefetch_related("company").values()
#     df = read_frame(qs)
#     df2 = read_frame(qs2)
#     df2.to_csv("result.csv")

#     dff =stats.get_CountryToConmpny()
#     for ind in dff.index:
#       print ( dff[ind])
      
   

  
    
    # return response.HttpResponse("hi")

