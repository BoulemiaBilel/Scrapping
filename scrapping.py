import requests
from bs4 import BeautifulSoup

url = 'https://www.emploilr.com/formation/annuaire/0.html' #on récupère l'url de la pemière page à scrapper, 15 centre par page, possibilité de fire une boucle pour tous les scrapper à la suite ?
reponse = requests.get(url)                                #on récupère le code html de la page dans reponse

if reponse.ok:                                              #test si le requests.get a bien fonctionné
    html = BeautifulSoup(reponse.text, features="html.parser")
    print(html)

