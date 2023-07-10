from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.home,name = 'bino'),
    path('binocalc',views.bins,name='bino_calc')
]
