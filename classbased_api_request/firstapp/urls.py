from django.urls import path,include
from firstapp.views import StuView,StuViewId

urlpatterns = [
    path('stu/',StuView.as_view()),
    path('stu/<int:id>/',StuViewId.as_view()),
]
