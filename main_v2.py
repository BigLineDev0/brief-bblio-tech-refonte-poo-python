from Models.abstract_document import Document
from Models.livre import Livre
from Models.magazine import Magazine
from Models.bibliothecaire import Bibliothecaire 
            
        
class Main:
    def __init__(self):
        self.bibliotheque = Bibliothecaire()

    def Menu(self):

        while True:
            print("\n", "-" * 10, "BIBLIOTHEQUE", "-" * 10)
            print("1: Ajouter Livre \n" \
            "2: Ajouter un magazine \n" \
            "3: Afficher le catalogue \n" \
            "4: Inscrire membres \n" \
            "5: Afficher membres \n" \
            "6: Valider pret \n" \
            "7: Afficher les emprunts d'un adherant \n"
            "8- Confirmer un retour\n"
            "0: Quitter")

            choix = input("\nEntrez votre choix : ")
            
            match choix:
                case "1":
                    try:
                        titre = input("titre : ")
                        if titre.isnumeric():
                            raise ValueError("le titre doit etre une chaine caractere ")
                        auteur = input("auteur : ")
                        
                        if auteur.isnumeric():
                            raise ValueError("l'auteur doit etre une chaine de caractere")
                        self.bibliotheque.ajouter_document(Livre(titre, auteur))
                    except ValueError as e:
                        print("ERREUR: ",e)

                case "2":
                    try:
                        titre = input("titre : ")
                        if titre.isnumeric():
                            raise ValueError("le titre doit etre une chaine caractere ")
                        auteur = input("auteur : ")
                        if auteur.isnumeric():
                            raise ValueError("l'auteur doit etre une chaine de caractere")
                        
                        frequence=input("frequence : ").lower()
                        if not frequence in ["hebdomadaire", "journaliere" ,"mensuelle"]:
                            raise ValueError("la frequence doit etre hebdomadaire, journaliere ou mensuelle")
                        
                        self.bibliotheque.ajouter_document(Magazine(titre, auteur, frequence))

                    except ValueError as e:
                        print("ERREUR: ",e)

                case "3":
                    self.bibliotheque.Lister_document()

                case '4':
                    try:
                        nom = input("Nom : ")
                        if nom.isnumeric():
                            raise ValueError('NOm invalide')
                        self.bibliotheque.InscrireMembre(nom)
                    except ValueError as e:
                        print("Erreur : ", e)

                case '5':
                    self.bibliotheque.Lister_membres()
                
                case '6':
                    print('------------------Liste des adherants-------------------')
                    self.bibliotheque.Lister_membres()
                    try:
                        
                        nom_membre=input("Nom: ")

                        if nom_membre.isnumeric():

                            raise ValueError("le nnom doit etre une chaine de caractere")
                    except ValueError as e:
                        print("Erreur : ", e)

                    print('------------------Liste des livres-------------------')
                    self.bibliotheque.Lister_document()
                    try:
                        titre_livre=input("Titre: ")
                        if titre_livre.isnumeric():
                            raise ValueError("le titre doit etre une chaine de cractere")
                        
                        self.bibliotheque.valider_pret(nom_membre,titre_livre)
                    except ValueError as e:
                        print("Erreur : ", e)

                case '7':
                    print('----------------Liste des adherants--------------')
                    self.bibliotheque.Lister_membres()
                    try:
                        nom=input('Nom: ')
                        if nom.isnumeric():
                            raise ValueError("le nom doit etre une chaine de caractere")
                        self.bibliotheque.Lister_Emprunt(nom)
                    except ValueError as e:
                        print("Erreur : ", e)

                case "8":
                    print('------------------Liste des documents-------------------')
                    self.bibliotheque.Lister_document()
                    try:
                        titre=input("titre: ")
                        if titre.isnumeric():
                            raise ValueError("le titre doit etre une chaine de caractere")
                        self.bibliotheque.confirmerRetour(titre)
                    except ValueError as e:
                        print("ERREUR : ", e)


                case '0':
                    print("BYE")
                    break  

                case _:
                    print("choix invalide")  

             
menu = Main()
menu.Menu()

    

        


                
                

                
            

        



