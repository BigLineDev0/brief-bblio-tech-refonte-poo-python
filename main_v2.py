from Models.abstract_document import Document
from Models.livre import Livre
from Models.magazine import Magazine
from Models.bibliothecaire import Bibliothecaire 
from Models.adherant import Adherant
from datetime import datetime
            
        
class Main:
    def __init__(self):
        self.bibliotheque = Bibliothecaire()


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
            print("1: Ajouter Livre \n" \
            "2: Ajouter un magazine \n" \
            "3: Afficher le catalogue \n" \
            "4: Inscrire membres \n" \
            "5: Afficher membres \n" \
            "6: Valider pret \n" \
            "7: Afficher les emprunts d'un adherant \n"
            "8: Confirmer un retour\n"
            "0: Quitter")

            choix = input("\nEntrez votre choix : ")
            
            match choix:
                case "1":
                    
                    try:
                        titre = validerChaine("Titre: ")

                        auteur = validerChaine("auteur: ")
                        type = input("type: ").upper()

                        if not type in ["LIVRE", "MAGAZINE"]:
                            raise ValueError("Type doit etre LIVRE ou MAGAZINE")

                        self.bibliotheque.ajouter_Livre(Livre(titre, auteur, type))
                        

                    except ValueError as e:
                        print("ERREUR: ",e)


                case "2":
                    try:
                        titre = validerChaine("Titre: ")

                        auteur = validerChaine("auteur: ")

                        type= input("type: ").upper()
                        frequence=input("frequence : ").lower()
                        if not frequence in ["hebdomadaire", "journaliere" ,"mensuelle"]:
                            raise ValueError("la frequence doit etre hebdomadaire, journaliere ou mensuelle")
                        
                        self.bibliotheque.ajouter_Magazine(Magazine(titre, auteur, type, frequence))

                    except ValueError as e:
                        print("ERREUR: ",e)

                case "3":
                    self.bibliotheque.Lister_document()

                case '4':
                    try:
                        nom = input("Nom : ")
                        if nom.isnumeric():
                            raise ValueError('NOm invalide')
                        # adherant=Adherant(nom)
                        self.bibliotheque.InscrireMembre(nom)
                    except ValueError as e:
                        print("Erreur : ", e)

                case '5':
                    self.bibliotheque.Lister_membres()
                
                case '6':
                   
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

                case "8":
                        
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

                case '0':
                    print("BYE")
                    break  

                case _:
                    print("choix invalide")  

             
menu = Main()
menu.Menu()     



