from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, ListAPIView

from companies.models import Company

from companies_api.serializers import CompanySerializer
# Create your views here.
class MobileCompanyView(ListAPIView):
    queryset = Company.objects.using("default").all()
    serializer_class = CompanySerializer
