from django.urls import path,include
from django.conf.urls import url
from appone.views import FileHandleView
urlpatterns = [

    path('upload/',FileHandleView.as_view()),

]
