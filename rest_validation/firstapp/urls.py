from django.urls import path
from .views import  BookView, ChapterViews

app_name = "app"
urlpatterns = [

    path("books/<int:pk>/", BookView.as_view(), name="books"),
    path("books/", BookView.as_view(), name="books"),
    path("chapters/", ChapterViews.as_view())
]
