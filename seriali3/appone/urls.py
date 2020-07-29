from django.urls import path
#from appone import views
from appone.views import MobileView, CompanyView


urlpatterns=[
        path('mobiles/',   MobileView.as_view()),
        path('company/', CompanyView.as_view())
               ]
