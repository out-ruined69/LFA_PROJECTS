import requests
from bs4 import BeautifulSoup
import re
url = "https://www.olx.ro/animale-de-companie/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")
page_text = doc.find(class_="block br3 brc8 large tdnone lheight24").span
span = str(page_text).split("/")
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])
nrpag = 25
links=[]
taguri=[]
for page in range(1,nrpag+1):
    url = f"https://www.olx.ro/animale-de-companie/?page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    div = doc.find(class_="fixed offers breakword redesigned")
    tags = div.find_all(["strong"])
    for tag in tags:
        taguri.append(tag)
t=[]
for tag in taguri:
    parent = tag.parent
    if parent.name == "a":
        if parent['href'] not in links:
            links.append(parent['href'])

def Filtrare(expresieREG):
    global links
    for link in links:
        page = requests.get(link).text
        doc = BeautifulSoup(page, "html.parser")
        if doc.find(text=re.compile(expresieREG))!=None:
            print(link)
Filtrare("[P,p]e[s,ș]te")
# Filtrare("[G,g][a,ă]in[ă,a,i]")
# Filtrare("[P,p]isic[a,ă]")
# Filtrare("[C,c][î,â,a]ine")
# Filtrare("[P,p]e[s,ș]te")
# Filtrare("[H,h]amster|i|")
# Filtrare("[I,i]epur[e,i]")
# Filtrare("[K,k]oi")
