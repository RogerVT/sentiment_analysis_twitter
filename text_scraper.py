from bs4 import BeautifulSoup
import pickle
import json 
import requests

features = []
file = open('./links_amlo.txt','r')
links = file.read().splitlines()
file.close()
counter = 1

for l in links:
   
    title = l[39:-1] 
    title = title.replace('-',' ').upper()
    date = l[28:38]
    date = date.replace('/','-')
    site = requests.get(l)
    sp = BeautifulSoup(site.content, 'html.parser')
    ps = sp.find_all('p')
    texts = [p.text for p in ps[:-2]]
    temp = {'index':counter, 'date':date, 'title':title, 'content':texts} 
    print(len(temp))
    features.append(temp)
    print("iter => ", counter)
    counter += 1

with open('./amlo_speech.json', 'w') as f:
    json.dump(features, f, sort_keys=True)

with open('./data_speech.pickle', 'wb') as f:
    pickle.dump(features, f)



#print(s[28:38])
#print(s[39:len(s)-1])