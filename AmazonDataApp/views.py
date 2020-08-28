from django.shortcuts import render
from django.http import HttpResponse
from AmazonDataApp.scrapping import get_data,compare_data
from AmazonDataApp.models import DataSheet

# Create your views here.
def busqueda_asin(request):
    

    return render(request,"AmazonDataApp/base.html")


def resultado_busqueda(request):
    producto = request.GET["prd"]
    if producto:
        lista=get_data(producto)
        comp = compare_data(producto,lista)

        return render(request,"AmazonDataApp/resultados.html",{"asin":producto, "lista":lista,"comp":comp})



    else:
        mensaje= "No se han encontrado productos"
    
    return HttpResponse(mensaje)


