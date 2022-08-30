
from django.urls import path

from travelapp import views

urlpatterns =[


    path('',views.demo,name='demo'),
]