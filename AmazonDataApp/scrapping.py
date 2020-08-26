from bs4 import BeautifulSoup
import requests

def get_data(asin):
    headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
}

    url = "https://www.amazon.es/dp/"+asin
    data_list=[]

    response = requests.post(url,headers=headers)

    if response.status_code == 200:
        texto = response.content
        soup = BeautifulSoup(texto,"lxml")
        respuesta = soup.find(class_="a-unordered-list a-vertical a-spacing-mini").find_all(class_="a-list-item")
        data_list.append(soup.title.text)
    for item in respuesta:
        data_list.append(item.text)
        
    return data_list




get_data("B07J6JGP52/")
