import requests
from bs4 import BeautifulSoup
import time
import re


liens = []                                                          
nom_organismes = [] 
descriptions = []
villes = []

"""
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

        #Villes organismes

        div_villes = html.find_all('div',{'class':'card bg-blue'})
        for div_ville in div_villes:
            villes.append(div_ville.find('span').text)
    

        #Desciptions oganismes
    
        card_aticle = html.find_all('div',{'class':'card__article'}) 
        
    
        for ca in card_aticle:
            descriptions.append(ca.text.strip()) 
    
        for i in range (len(descriptions)):
            descriptions[i] = descriptions[i].replace('\r','').replace('\n','')
    
        
        liens_orga = []
        for cda in card_info:
            liens_orga.append(cda.find('a',{'class':'card__link card__link--sm'}))
        for k in liens_orga:
            lien=k['href']
            liens.append(lien)

        time.sleep(3)

with open('urls.txt', 'w') as file:
    for lien in liens:
        file.write(lien + '\n')
"""
code_postal = []
adresses = []
telephones = []


with open('urls.txt', 'r') as file:
    for row in file:
        url = row.strip()

        reponse = requests.get(url)
        if reponse.ok:
            html = BeautifulSoup(reponse.text, features = "html.parser")

            divcardbody = html.find_all('div',{'class':'business-card__body'})
            for p in divcardbody:
                infos = []
                infos.append(p.text)
                adresse_regex = r'\d{1,3}\s[\w\s]+\n'
                code_postal_regex = r'\d{5}'
                telephone_regex = r'Tel\s:\s(\d{2}\.\d{2}\.\d{2}\.\d{2})'

                adresse = re.search(adresse_regex, infos[0]).group(0).strip()
                codepostal = re.search(code_postal_regex, infos[0]).group(0)
                telephone = re.search(telephone_regex, infos[0]).group(1)

                code_postal.append(codepostal)
                adresses.append(adresse)
                telephones.append(telephone)

            
print (code_postal)
print (adresses)
print (telephones)