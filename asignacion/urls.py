from django.urls import path

from .import views 

urlpatterns = [
    
    path('',views.procesar_asignacion, name="procesar_asignacion")


    
]