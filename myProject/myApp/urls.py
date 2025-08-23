from django.urls import path
# . represents current diretory here
from . import views

urlpatterns = [
    path('', views.all_myApp, name = 'myApp_home'),
    
]