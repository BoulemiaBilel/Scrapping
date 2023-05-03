import requests
from bs4 import BeautifulSoup

url = 'https://www.emploilr.com/formation/annuaire/0.html' 
reponse = requests.get(url)                                

if reponse.ok:                                             
    html = BeautifulSoup(reponse.text, features="html.parser") 
    
    #Nom des organismes 

    card_info = html.find_all('div',{'class':'card__info'})                         #On récupère dans une liste card_info toutes les div de cette classe                         
    
    nom_organismes_a = []                                                           #On initialise une liste vide qui contiendra toutes les balises a de chaque div de la classe précédente car le nom de l'oganisme se trouve dans cette balise a
    nom_organisme = []                                                              #On initialise la liste finale qui contiendra les noms de chaque organisme
    
    for cd in card_info:
        nom_organismes_a.append(cd.find('a',{'class':'card__link card__link--sm'})) 
    
    for cda in nom_organismes_a:
        nom_organisme.append(cda.text.strip())
    
    print (nom_organisme)

    #Desciptions oganismes
    
    card_aticle = html.find_all('div',{'class':'card__article'}) 
    descriptions = []
    
    for ca in card_aticle:
        descriptions.append(ca.text.strip()) 
    
    for i in range (len(descriptions)):
        descriptions[i] = descriptions[i].replace('\r','').replace('\n','')
    
    print(descriptions)
     
    
     
    #nom_organismes = card_info.find('a', {'class':'card__link card__link--sm'})
    #description = html.find_all('div',{'class':'card__article'})
    
    #print (nom_organismes)
    


        

