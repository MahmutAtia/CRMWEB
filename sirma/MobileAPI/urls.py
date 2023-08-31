from django.urls import path
from .views import MobileCompanyView, MobileCountryList,MobileContactApiCL,MobileContactResultList,MobileTodayContactApiCL

app_name = "mobile-api"
urlpatterns = [
    path("<int:user>/<country>/<int:num>",MobileCompanyView.as_view()),
    path("country",MobileCountryList.as_view()),
    path("company/<int:pk>", MobileContactApiCL.as_view()),
    path("results", MobileContactResultList.as_view()),
    path("today", MobileTodayContactApiCL.as_view()),
   
    
]