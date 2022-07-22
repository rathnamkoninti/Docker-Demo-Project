from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('demo/',views.demo,name='demo'),
    path('welcome/',views.welcome,name='welcome'),

]