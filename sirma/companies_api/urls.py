from django.urls import path
from .views import weekly_report_as_text  ,CheckCompanyName, check_company_name, MyDataFrameAPIView,CompanyApiCL,CompanyApiRUD,ContactApiCL,ContactApiRUD,CountryList, ContactResultList, ContactTypeList

app_name = "companies-api"
urlpatterns = [
    path('', CompanyApiCL.as_view()),
    path('<int:pk>', CompanyApiRUD.as_view(), name = "company-details"),
    path('company/<int:pk>', ContactApiCL.as_view(), name = "contact-history"),
    path('contact/<int:pk>', ContactApiRUD.as_view(), name = "contact-details"),
    path('country',CountryList.as_view()),
    path('contact_result',ContactResultList.as_view()),
    path('contact_type',ContactTypeList.as_view()),
    path('analitics/<int:days>/<int:user_id>',MyDataFrameAPIView.as_view()),
    path('report',weekly_report_as_text),
    path('check_company_name/',check_company_name), # You need to enable JavaScript to run this app. because you didnt put this




    


    
]