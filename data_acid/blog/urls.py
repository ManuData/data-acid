


from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"), 
    path('feedback/', views.leads_form, name='leads_form')
] 

