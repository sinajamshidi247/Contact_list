from django.urls import path 
from . import views

app_name = 'contact'

urlpatterns = [
    path('',views.index,name = "index"),
    path('add/',views.add,name = "add"),
    path('contact-profile/<int:pk>/',views.cotact_profile,name = "profile"),


]