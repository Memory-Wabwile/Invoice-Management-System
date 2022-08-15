from django.urls import path
from . import views


urlpatterns = [
    path('', views.home , name = "home"),
    path('add_invoice/', views.add_invoice , name = "add_invoice"),
    
]