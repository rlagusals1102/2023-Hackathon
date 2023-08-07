from django.urls import path
from .views import *

app_name='main'

urlpatterns=[
    path('', index),
    path('send/', sendView),
    path('send/<int:id>', sendCtrl),
    path('hospitals/', markHospital),
]