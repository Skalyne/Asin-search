from django.contrib import admin
from django.urls import path

from AmazonDataApp import views #que no se olvide

urlpatterns = [
    path('',views.busqueda_asin, name="get_data"),
    path("buscar/",views.resultado_busqueda),
    path("buscardb/",views.resultado_busqueda_db),]