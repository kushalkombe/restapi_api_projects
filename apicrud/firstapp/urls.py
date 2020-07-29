from django.urls import path
from firstapp import views
from firstapp.views import EmployeeListModelMixin, EmployeeDetailAPIViewMixin

urlpatterns = [

    path('api/', EmployeeListModelMixin.as_view()),
    path('api/<int:pk>/', EmployeeDetailAPIViewMixin.as_view()),
]
