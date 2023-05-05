import requests
from bs4 import BeautifulSoup
import time

liens = []                                                          
nom_organismes = [] 
descriptions = []

for i in range (0, 32, 15):
    url = 'https://www.emploilr.com/formation/annuaire/' + str(i) +'.html'
    print(url)
    reponse = requests.get(url)                                

    if reponse.ok:                                             
        html = BeautifulSoup(reponse.text, features="html.parser") 
    
        #Nom des organismes 

        card_info = html.find_all('div',{'class':'card__info'})                                                  
    
        nom_organismes_a = []
        
        for cd in card_info:
            nom_organismes_a.append(cd.find('a',{'class':'card__link card__link--sm'})) 
    
        for cda in nom_organismes_a:
            nom_organismes.append(cda.text.strip())
    

        #Desciptions oganismes
    
        card_aticle = html.find_all('div',{'class':'card__article'}) 
        
    
        for ca in card_aticle:
            descriptions.append(ca.text.strip()) 
    
        for i in range (len(descriptions)):
            descriptions[i] = descriptions[i].replace('\r','').replace('\n','')
    
        #print(descriptions)
        liens_orga = []
        for cda in card_info:
            liens_orga.append(cda.find('a',{'class':'card__link card__link--sm'}))
        for k in liens_orga:
            lien=k['href']
            liens.append(lien)

        time.sleep(3)

print(nom_organismes)
print(len(liens))
print(len(descriptions))
    

#il me reste à parcourir les liens pour avoir les infos tel l'adresse le CP, le numéro de tel le mail et le nom du contact
        

