import requests
from bs4 import BeautifulSoup as bs
import json


doctissimoURL = "https://www.doctissimo.fr/asp/medicaments/les-medicaments-les-plus-prescrits.htm"

def scrapeMedicaments(url):

    fullpage = requests.get(url).content
    soup1 = bs(fullpage, "lxml")

    liste_medicaments = soup1.findAll("ul", class_="doc-list doc-list--arrow-right")[14]

    
    for a in liste_medicaments.findAll("a"):
        symptomes = []
        page_medicament = requests.get(a["href"]).content
        soup2 = bs(page_medicament, "lxml")
        titre_medicament = soup2.find("h1").text.split(",")
        symptomes_medicament = soup2.findAll("ul", class_="doc-list doc-list--arrow-right")[14]
        for s1 in symptomes_medicament.findAll("li"):
            for s2 in s1.find_all():
                symptomes.append(s2.text.replace("\n", ""))



        medicament = {
            "nom" : titre_medicament[0],
            "type" : titre_medicament[1],
            "description" : titre_medicament[2],
            "symptomes" : symptomes,
            "prise" : 'NA',
        }
        print(medicament)
    return medicament

        

scrapeMedicaments(doctissimoURL)