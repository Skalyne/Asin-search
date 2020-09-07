from bs4 import BeautifulSoup
import requests
from AmazonDataApp.models import DataSheet
from django.db import models



def get_data(asin):
    header_list=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
    'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0;  Trident/5.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; MDDCJS)',
    'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G570Y Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900 Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-N910F Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7',
    'Mozilla/5.0 (Linux; Android 7.0; HTC 10 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36',
    'Lynx/2.8.8pre.4 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.12.23',
    'Wget/1.15 (linux-gnu)',
    'curl/7.35.0']

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
    



def db_query(asin):
    try:
        comp = DataSheet.objects.filter(asin=asin).order_by("-query_date")
    except:
        comp=["no hay registros previos o no es un asin válido"]
  
    return comp

