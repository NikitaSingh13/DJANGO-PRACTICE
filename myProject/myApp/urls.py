from django.urls import path
# . represents current diretory here
from . import views

urlpatterns = [
    path('', views.all_myApp, name = 'myApp_home'),
    path('<int:user_id>/', views.user_discription, name='user_discription'),
    path('user_forms/', views.user_forms, name='user_forms')
    
]