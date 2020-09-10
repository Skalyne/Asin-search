from bs4 import BeautifulSoup
import requests
from AmazonDataApp.models import DataSheet
from django.db import models
from AmazonDataApp.resources.headers import header_list



def get_data(asin):

    url = "https://www.amazon.es/dp/"+asin
    data_list=[]

    header_position = 0
    headers={'User-Agent': header_list[header_position]}
    respuesta = False

    while not respuesta:
        if header_position >= (len(header_list)-1):
            data_list=["No se encontraron datos para este ASIN"]
            break
        try:
            response = requests.post(url,headers=headers)
            if response.status_code == 200:
                texto = response.content
                soup = BeautifulSoup(texto,"lxml")
                respuesta = soup.find(class_="a-unordered-list a-vertical a-spacing-mini").find_all(class_="a-list-item")
                data_list.append(soup.title.text)
                for item in respuesta:
                    data_list.append(item.text)
        except:
            header_position+=1

    return data_list


def compare_data(asin,lista):
    try:
        comp = DataSheet.objects.filter(asin=asin).order_by("-query_date")
        if (lista[0]==comp[0].titulo and lista[1]==comp[0].bullet_1 and lista[2]==comp[0].bullet_2 and lista[3]==comp[0].bullet_3 and lista[4]==comp[0].bullet_4 and lista[5]==comp[0].bullet_5):
            pass            
        else:
            as1=DataSheet(asin=asin, titulo=lista[0],bullet_1=lista[1],bullet_2=lista[2],bullet_3=lista[3],bullet_4=lista[4],bullet_5=lista[5])
            as1.save()
    except:
        try:
            as1=DataSheet(asin=asin, titulo=lista[0],bullet_1=lista[1],bullet_2=lista[2],bullet_3=lista[3],bullet_4=lista[4],bullet_5=lista[5])
            as1.save()
            comp=["no hay registros previos"]
        except:
            comp =["No es un asin valido"]    
    return comp
    

def compare_data2(asin,lista):
    if DataSheet.objects.filter(asin=asin).order_by("-query_date"):
        if (lista[0]==comp[0].titulo and lista[1]==comp[0].bullet_1 and lista[2]==comp[0].bullet_2 and lista[3]==comp[0].bullet_3 and lista[4]==comp[0].bullet_4 and lista[5]==comp[0].bullet_5):
            pass
        



def db_query(asin):
    try:
        comp = DataSheet.objects.filter(asin=asin).order_by("-query_date")
    except:
        comp=["no hay registros previos o no es un asin válido"]
  
    return comp

