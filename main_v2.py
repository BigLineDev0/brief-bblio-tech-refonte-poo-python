from Models.abstract_document import Document
from Models.livre import Livre
from Models.magazine import Magazine
from Models.bibliothecaire import Bibliothecaire 
from Models.adherant import Adherant
from datetime import datetime
import bcrypt
from Models.authentification import Authentification
            
        
class Main:
    def __init__(self):
        self.bibliotheque = Bibliothecaire()
        self.user_connect = None



    def Menu_authentification(self):
        while True:

            print("\n", "-" * 10, "AUTHENTIFICATION", "-" * 10)
            print("1- S'inscire\n" \
                 "2- Se connecter\n")
            
            choix=input("\nVotre Choix: ")

            match choix:
                case "1":
                    nom=input("Nom: ").strip()
                    prenom=input("Prenom: ").strip()
                    email=input("Email: ").strip()
                    password=input("Mot de passe: ").encode().strip()
                    passwordHash=bcrypt.hashpw(password, bcrypt.gensalt())
                    self.bibliotheque.inscription(Authentification(nom,prenom,email,passwordHash))

                case "2":
                    email=input("Email: ")
                    password=input("Mot de passe: ")
                    self.user_connect = self.bibliotheque.connexion(email,password)
                    if self.user_connect:
                        self.Menu()
                    else:
                        print("ERREUR CONNEXION")
                        self.Menu_authentification()
                case _: 
                    print("Choix invalide")

    def Menu(self):

    
        def validerChaine(valeur):
            while True:
                valeur=input(valeur).strip()
                if valeur == "":
                    print("La valeur ne peut pas être vide.")
                    continue

                if valeur.isnumeric():
                    print("La valeur ne doit pas être uniquement composée de chiffres.")
                    continue

                return valeur
                        
        while True:
            print("\n", "-" * 10, "BIBLIOTHEQUE", "-" * 10)
            print("1: Ajouter un document \n" \
            "2: Afficher documents \n" \
            "3: Inscrire membres \n" \
            "4: Afficher membres \n" \
            "5: Valider pret \n" \
            "6: Confirmer un retour\n"
            "7: Afficher les emprunts d'un adherant \n"
            "0: Quitter")

            choix = input("\nEntrez votre choix : ")
            
            match choix:
                case "1":
                    
                    try:
                        titre = validerChaine("Titre : ")

                        auteur = validerChaine("Auteur : ")
                        type = input("Type : ").upper()

                        if not type in ["LIVRE", "MAGAZINE"]:
                            raise ValueError("Type doit etre LIVRE ou MAGAZINE")
                        
                        if type == "LIVRE":

                            self.bibliotheque.ajouter_Livre(Livre(titre, auteur, type))

                        if type == "MAGAZINE":
                            frequence=input("Frequence : ").lower()
                            if not frequence in ["hebdomadaire", "journaliere" ,"mensuelle"]:
                                raise ValueError("la frequence doit etre hebdomadaire, journaliere ou mensuelle")
                            
                            self.bibliotheque.ajouter_Magazine(Magazine(titre, auteur, type, frequence))

                    except ValueError as e:
                        print("ERREUR: ",e)

                case "2":
                    self.bibliotheque.Lister_document()

                case '3':
                    try:
                        nom = input("Nom Membre: ")
                        if nom.isnumeric():
                            raise ValueError('NOm invalide')
                        
                        self.bibliotheque.InscrireMembre(Adherant(nom))
                    except ValueError as e:
                        print("Erreur : ", e)

                case '4':
                    self.bibliotheque.Lister_membres()
                
                case '5':
                   
                    print('------------------Liste des adherants-------------------')
                    self.bibliotheque.Lister_membres()
                    try:
                        id_membre=input("ID adhérant: ")

                        if not id_membre.isnumeric():

                            raise ValueError("l'id doit etre un chiffre")
                    except ValueError as e:
                        print("Erreur : ", e)

                    print('------------------Liste des livres-------------------')
                    self.bibliotheque.Lister_document()
                    try:
                        id_document=input("ID du documeent: ")
                        if not id_document.isnumeric():
                            raise ValueError("l'Id' doit etre une chaine de cractere chiffre")
                        
                    except ValueError as e:
                        print("Erreur : ", e)


                    try:
                        dateretourprogramme = input("date retour programme (YYYY/MM/DD): ")
                        
                        dateconvert = datetime.strptime(dateretourprogramme, "%Y/%m/%d")

                        dateMysql = dateconvert.strftime("%Y-%m-%d")
                        
                        self.bibliotheque.valider_pret(id_membre,id_document,dateMysql)
                        
                    except ValueError:
                        print("Format invalide. Utilise YYYY/MM/DD")

                case "6":
                        
                    print('----------------Liste des adherants--------------')
                    self.bibliotheque.Lister_membres()
                    try:

                        id_membre=input("ID MEMBRE: ")
                        if not id_membre.isnumeric():
                            raise ValueError("L'id doit etre un chiffre")
                    except ValueError as e:
                        print("ERREUR : ", e)   

                    print('------------------Liste des documents-------------------')
                    self.bibliotheque.Lister_document()
                    
                    try:
                        id_document=input("id_document: ")
                        if not id_document.isnumeric():
                            raise ValueError("l' id_document doit etre un chiffre")

                    except ValueError as e:
                        print("ERREUR : ", e) 

                    self.bibliotheque.confirmerRetour(id_membre, id_document)

                case '7':
                    print('----------------Liste des adherants--------------')
                    self.bibliotheque.Lister_membres()
                    try:
                        id_adherant=input('id_adherant: ')
                        if not id_adherant.isnumeric():
                            raise ValueError("le id_adherant doit etre un chiffre")
                        self.bibliotheque.Lister_Emprunt(id_adherant)
                    except ValueError as e:
                        print("Erreur : ", e)

                case '0':
                    print("BYE")
                    break  

                case _:
                    print("choix invalide")  


            
menu = Main()
menu.Menu_authentification()     



