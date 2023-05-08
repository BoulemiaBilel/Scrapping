import requests
from bs4 import BeautifulSoup
import time
import re


liens = []                                                         
nom_organismes = [] 
descriptions = []
villes = []

for i in range (0, 32, 15):
    url = 'https://www.emploilr.com/formation/annuaire/' + str(i) +'.html'
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

print(liens)      

cp = []
adresses = []
telephones = []
sites = []
courriels = []


with open('urls.txt', 'r') as file:
    for row in file:
        url = row.strip()

        reponse = requests.get(url)
        if reponse.ok:
            html = BeautifulSoup(reponse.text, features = "html.parser")

        divcardbody = html.find_all('div',{'class':'business-card__body'})
        for p in divcardbody:
            infos = []
            infos = (p.text).split('\n')
            new_infos = list(filter(lambda x: x != '', infos))

            if (len(new_infos) == 5):
        
                #Adresse
                adresse = new_infos[0]
                adresses.append(adresse)
            

        
                #Code postal
                cpville = new_infos[1]
                code_postal_regex = r'\b(\d{5})\b'
                code_postal = re.search(code_postal_regex, cpville).group(1)
                cp.append(code_postal)

                #Telephone
                tel = new_infos[2]
                tel_regex = r'Tel : (.*)'
                tel = re.search(tel_regex, tel).group(1)
                telephones.append(tel)

                #Courriel
                courr = new_infos[3]
                courr_regex = r'[\w\.-]+@[\w\.-]+'
                courriel = re.search(courr_regex, courr).group(0)
                courriels.append(courriel)

                #Site
                site = new_infos[4]
                site_regex = r'Site : (http.*$)'
                site = re.search(site_regex, site).group(1)
                sites.append(site)
        
            else:
                #Adresse
                adresse = new_infos[0]
                adresses.append(adresse)

                #Code postal
                cpville = new_infos[1]
                code_postal_regex = r'\b(\d{5})\b'
                code_postal = re.search(code_postal_regex, cpville).group(1)
                cp.append(code_postal)

                #Telephone
                tel = new_infos[2]
                tel_regex = r'Tel : (.*)'
                tel = re.search(tel_regex, tel).group(1)
                telephones.append(tel)

                #Courriel
                courriels.append('None')

                #Site
                site = new_infos[3]
                site_regex = r'Site : (http.*$)'
                site = re.search(site_regex, site).group(1)
                sites.append(site)

print(len(cp))
print(len(adresses))
print(len(telephones))
print(len(courriels))
print(len(sites))





        
        

        

        
    
                
                

            
