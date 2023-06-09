from django.urls import path
from .views import  MyDataFrameAPIView,CompanyApiCL,CompanyApiRUD,ContactApiCL,ContactApiRUD,CountryList, ContactResultList, ContactTypeList

app_name = "companies-api"
urlpatterns = [
    path('', CompanyApiCL.as_view()),
    path('<int:pk>', CompanyApiRUD.as_view(), name = "company-details"),
    path('company/<int:pk>', ContactApiCL.as_view(), name = "contact-history"),
    path('contact/<int:pk>', ContactApiRUD.as_view(), name = "contact-details"),
    path('country',CountryList.as_view()),
    path('contact_result',ContactResultList.as_view()),
    path('contact_type',ContactTypeList.as_view()),
    path('analitics/<int:days>',MyDataFrameAPIView.as_view()),



    


    
]