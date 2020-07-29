from django.urls import path
from firstapp.views import emp,emp_details
urlpatterns = [
    path('emp/',emp),
    path('emp/<int:id>',emp_details),
]
