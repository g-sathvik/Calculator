from django.contrib import admin
from django.urls import path,re_path
from . import views
urlpatterns = [
    
    path('',views.home,name = 'black'),	
    path('blackScholes',views.bs,name='blac_calc')
]
