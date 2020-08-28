from django.shortcuts import render
from django.http import HttpResponse
from AmazonDataApp.scrapping import get_data
from AmazonDataApp.models import DataSheet

# Create your views here.
def busqueda_asin(request):
    

    return render(request,"AmazonDataApp/base.html")


def resultado_busqueda(request):
    producto = request.GET["prd"]
    if producto:

            lista=get_data(producto)
            as1=DataSheet(asin=producto, titulo=lista[0],bullet_1=lista[1],bullet_2=lista[2],bullet_3=lista[3],bullet_4=lista[4],bullet_5=lista[5])
            as1.save()
            return render(request,"AmazonDataApp/resultados.html",{"asin":producto, "lista":lista})

    else:
        mensaje= "No se han encontrado productos"
    
    return HttpResponse(mensaje)


