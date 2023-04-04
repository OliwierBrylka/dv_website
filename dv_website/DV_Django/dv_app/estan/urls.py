from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('estan',views.e_stan, name='estan'),
]