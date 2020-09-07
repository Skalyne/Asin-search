from django.shortcuts import render
from django.http import HttpResponse
from AmazonDataApp.scrapping import get_data,compare_data,db_query
from AmazonDataApp.models import DataSheet
from openpyxl import Workbook


# Create your views here.
def busqueda_asin(request):

    return render(request,"AmazonDataApp/base.html")


def resultado_busqueda(request):
    producto = request.GET["prd"]
    lista=[]
    if len(producto)==10:
        lista=get_data(producto)
        comp = compare_data(producto,lista)
    else:
        comp=["no es un asin válido"]
    return render(request,"AmazonDataApp/resultados.html",{"asin":producto, "lista":lista,"comp":comp})



def resultado_busqueda_db(request):
    producto = request.GET["prddb"]
    if len(producto)==10:
        comp=db_query(producto)
    else:
        comp=["no es un asin válido"]
    return render(request,"AmazonDataApp/resultados.html",{"asin":producto,"comp":comp})
    
