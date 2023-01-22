from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('home/',views.homeView,name='homeView'),
    path('add/',views.addView,name='addView'),
    path('delete/<str:id>',views.deleteView,name='deleteView'),
    path('edit/<str:id>',views.editView,name='editView'),
    
]