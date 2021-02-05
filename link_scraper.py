from bs4 import BeautifulSoup
import requests

url = 'https://lopezobrador.org.mx/transcripciones/'
site = requests.get(url)
sp = BeautifulSoup(site.content, 'html.parser')
links = sp.find_all('h2', class_='entry-title')
res = [link.find('a')['href'] for link in links]
counter = len(res)
url_base = 'https://lopezobrador.org.mx/transcripciones/page/'
for i in range(2, 176):
    #print('it =>', i)
    temp_u = url_base +str(i)+'/'
    site = requests.get(temp_u)
    sp = BeautifulSoup(site.content, 'html.parser')
    temp_links = sp.find_all('h2', class_='entry-title')
    temp = [link.find('a')['href'] for link in temp_links]
    counter += len(temp)
    res += temp
    temp.clear()

with open('./links_amlo.txt', 'w') as f:
    for i in res:
        f.write("%s\n" % i)

print("size counter =>", counter)
print("act_size =>", len(res))
