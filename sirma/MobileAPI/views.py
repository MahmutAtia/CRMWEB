from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, ListAPIView

from companies.models import Company, Country,Contact,ContactResult

from companies_api.serializers import CompanySerializer, CountrySerializer,ContactSerializer,ContactResultSerializer
# Create your views here.

import datetime

class MobileCompanyView(ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):

        user = self.kwargs["user"]
        country_from_req = self.kwargs["country"]
        num = self.kwargs["num"] * 10

        # get the forgnkey
        country = Country.objects.filter(name=country_from_req).first()

        if country_from_req == "all":

            queryset = Company.objects.using("default").filter(
                user=user,
            ).order_by("-status")[:num]

        else:
            queryset = Company.objects.using("default").filter(
                user=user,
                country=country).order_by("-status")[:num]

        return queryset


class MobileCountryList(ListCreateAPIView):
    serializer_class = CountrySerializer
    


# you can use this method to filter the queryset for defferent users 
# very important
    def get_queryset(self):
        qs = Country.objects.using("default").filter( company__user = 2).distinct()
        return qs


class MobileContactResultList(ListCreateAPIView):
    serializer_class = ContactResultSerializer
    queryset = ContactResult.objects.using("default").all()





class MobileContactApiCL(ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.using("default").all()


    def get_queryset(self):
        print("get_queryset")
        pk = self.kwargs["pk"]
        qs = Contact.objects.using("default").filter(company__pk = pk)
   
        return qs


class MobileTodayContactApiCL(ListCreateAPIView):
    serializer_class = ContactSerializer
    



# you can use this method to filter the queryset for defferent dates
    def get_queryset(self):
        date = datetime.datetime.now().date()
        queryset = Contact.objects.using("default").filter(date=date)
        return queryset



   
