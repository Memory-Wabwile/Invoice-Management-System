from django.urls import path
from . import views


urlpatterns = [
    path('', views.home , name = "home"),
    path('search/', views.add_invoice , name = "search"),
    
]