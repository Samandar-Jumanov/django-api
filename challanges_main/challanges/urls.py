from  django.urls import path
from . import  views


urlpatterns = [
  path("", views.get_links),
  path("", views.get_names),
  path('<int:month>', views.month_number),
  path('<str:month>', views.months, name='challanges')
]


