from django.urls import path
#from appone import views
from .views import BookView, ChapterView


urlpatterns=[
        path('books/',   BookView.as_view()),
        path('chapters/', ChapterView.as_view())
               ]
