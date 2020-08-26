from django.shortcuts import render
from django.http import HttpResponse
from AmazonDataApp.scrapping import get_data

# Create your views here.
def busqueda_asin(request):
    

    return render(request,"AmazonDataApp/search.html")


def resultado_busqueda(request):
    producto = request.GET["prd"]
    if producto:

            list=get_data(producto)
            return render(request,"AmazonDataApp/resultados.html",{"asin":producto, "lista":list})

    else:
        mensaje= "No se han encontrado productos"
    
    return HttpResponse(mensaje)


