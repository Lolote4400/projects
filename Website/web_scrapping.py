import requests
from bs4 import BeautifulSoup
import csv

    # En-têtes pour simuler un navigateur
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0"
}


# Extraction page Cuisine dauphinoise
    # URL de la page Wikipédia sur les Cuisine dauphinoise
url = "https://fr.wikipedia.org/wiki/Cuisine_dauphinoise"

    # Récupérer le contenu de la page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

    # Dictionnaire pour stocker l'ensemble des données extraites
donnees_cuisine_dauphinoise = []

    # Extraction des données du paragraphe Noix de Grenoble
donnees_section1 = {}

        #Extraction du titre de la section
titre_section1 = soup.find("h4", {"id": "Noix_de_Grenoble"})
donnees_section1["Titre"] = titre_section1.get_text(strip=True)

        #Extraction d'un paragraphe de la section
contenu_section1 = titre_section1.find_next("p")
donnees_section1["Contenu"] = contenu_section1.get_text(strip=True)


    # Extraction des données du paragraphe Fromage
donnees_section2 = {}

        #Extraction du titre de la section
titre_section2 = soup.find("h3", {"id": "Fromage"})
donnees_section2["Titre"] = titre_section2.get_text(strip=True)

        # Extraire le texte de chaque élément <li> de la liste
liste_section2 = titre_section2.find_next("ul")
elements_liste = [li.get_text(strip=True) for li in liste_section2.find_all("li")]
donnees_section2["Liste"] = "\n".join(elements_liste)


    # Extraction des données du paragraphe Chartreuse verte et jaune
donnees_section3 = {}

        #Extraction du titre de la section
titre_section3 = soup.find("h4", {"id": "Chartreuse_verte_et_jaune"})
donnees_section3["Titre"] = titre_section3.get_text(strip=True)

        #Extraction d'un paragraphe de la section
contenu_section3 = titre_section3.find_next("p")
donnees_section3["Contenu"] = contenu_section3.get_text(strip=True)


    # Extraction des données du paragraphe Ravioles du Dauphiné
donnees_section4 = {}

        #Extraction du titre de la section
titre_section4 = soup.find("h4", {"id": "Ravioles_du_Dauphiné"})
donnees_section4["Titre"] = titre_section4.get_text(strip=True)

        #Extraction d'un paragraphe de la section
contenu_section4 = soup.find("a", {"title": "Raviole du Dauphiné"})

if contenu_section4.get('href').startswith("/"):
    lien_raviole = "https://fr.wikipedia.org" + lien_section4.get('href')
else:
    lien_raviole = contenu_section4.get('href')
donnees_section4["Contenu"] = f"Voir données extraites du site {lien_raviole}"


    #Ajout des données extraites au dictionnaire donnees_cuisine_dauphinoise
donnees_cuisine_dauphinoise.append(donnees_section1)
donnees_cuisine_dauphinoise.append(donnees_section2)
donnees_cuisine_dauphinoise.append(donnees_section3)
donnees_cuisine_dauphinoise.append(donnees_section4)


    # Chemin relatif pour enregistrer le fichier CSV
chemin_csv1 = "../data/cuisine_dauphinoise.csv"

    # Sauvegarde des données extraites dans un fichier CSV
with open(chemin_csv1, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Titre', 'Contenu', 'Liste'])
    writer.writeheader()
    writer.writerows(donnees_cuisine_dauphinoise)

print(f"Sections extraites et enregistrées dans {chemin_csv1}")



# Extraction page Ravioles du Dauphiné

    # URL de la page Wikipédia sur les Ravioles du Dauphiné
url = "https://fr.wikipedia.org/wiki/Raviole_du_Dauphin%C3%A9"

    # Récupérer le contenu de la page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

    # Dictionnaire pour stocker l'ensemble des données extraites
donnees_ravioles = []

    # Extraction des données du paragraphe Localisation Géographique
donnees_section1 = {}

      #Extraction du titre de la section
titre_section1 = soup.find("h2", {"id": "Localisation_géographique"})
donnees_section1["Titre"] = titre_section1.get_text(strip=True)

        #Extraction d'un paragraphe de la section
contenu_section1 = titre_section1.find_next("p")
donnees_section1["Contenu"] = contenu_section1.get_text(strip=True)


      #Extraction de l'image de la section
image = soup.find("h2", {"id": "Localisation_géographique"}).find_next("img")
image_url = ""

if image["src"].startswith("//"):
    image_url = "https:" + image_url
else: 
    image_url = image["src"]
donnees_section1["Image"] = image_url


    # Extraction des données du paragraphe Composition et fabrication
donnees_section2 = {}

       #Extraction du titre de la section
titre_section2 = soup.find("h3", {"id": "Composition_et_fabrication"})
donnees_section2["Titre"] = titre_section2.get_text(strip=True)

       #Extraction des 2 premiers paragraphes de la section
contenu_section2 = []
contenu2 = titre_section2.find_next("p")
for _ in range(2):
    contenu_section2.append(contenu2.get_text(strip=True))
    contenu2 = contenu2.find_next("p")

donnees_section2["Contenu"] = "\n".join(contenu_section2)

    # Extraction des données du paragraphe Consommation
donnees_section3 = {}

       #Extraction du titre de la section
titre_section3 = soup.find("h2", {"id": "Consommation"})
donnees_section3["Titre"] = titre_section3.get_text(strip=True)

      #Extraction des 2 premiers paragraphes de la section
contenu_section3 = []
contenu3 = titre_section3.find_next("p")
for _ in range(2):
    contenu_section3.append(contenu3.get_text(strip=True))
    contenu3 = contenu3.find_next("p")

donnees_section3["Contenu"] = "\n".join(contenu_section3)


    #Ajout des données extraites au dictionnaire donnees_ravioles
donnees_ravioles.append(donnees_section1)
donnees_ravioles.append(donnees_section2)
donnees_ravioles.append(donnees_section3)


    # Chemin relatif pour enregistrer le fichier CSV
chemin_csv2 = "../data/raviole_du_dauphine.csv"

    # Sauvegarde des données extraites dans un fichier CSV
with open(chemin_csv2, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Titre', 'Contenu', 'Image'])
    writer.writeheader()
    writer.writerows(donnees_ravioles)

print(f"Sections extraites et enregistrées dans {chemin_csv2}")
