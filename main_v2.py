from abc import ABC, abstractmethod
class Document(ABC):
    def __init__(self,titre,auteur,disponible=True):
        self.titre = titre
        self.auteur = auteur
        self.__disponible = disponible

    @property
    def disponible(self):
        return self.__disponible
    
    @disponible.setter
    def disponible(self, valeur):
        self.__disponible = valeur
        return self.__disponible

    @abstractmethod
    def emprunter(self):
        pass
    
    @abstractmethod
    def retourner(self):
        pass    

class Livre(Document):
    def __init__(self, titre, auteur, disponible=True):
        super().__init__(titre, auteur, disponible)
    
    def emprunter(self):
        if not self.disponible:
            print(f"Le livre {self.titre} est deja emprunte")
        else:
            self.disponible = False
            print('Livre emprunte avec succès.')
            
    def retourner(self):
        if self.disponible:
            print("Ce livre n'est pas encore emprunté impossible de retourner")
            return
        
        self.disponible = True
        print("Livre retourné avec succès.")
    
    def __str__(self):
       
        if self.disponible == True:
            dispo = "Disponible"
        else:
            dispo = "Emprunté"
        return f"Livre: {self.titre} - Auteur: {self.auteur} - Statut:[{dispo}]"

    
class Magazine(Document):
    def __init__(self, titre, auteur, frequence ,disponible=True):
        super().__init__(titre, auteur, disponible)
        self.frequence=frequence

    def emprunter(self):
        if not self.disponible:
            print(f"Ce Magazine {self.titre} n'est pas encore retouné")
        else:
            self.disponible = False
            print('Magazine emprunte avec succès.')
            
    
    def retourner(self):
        if self.disponible:
            print("Magazine n'est pas encore emprunté impossible de retourner")
            return
        
        self.disponible = True
        print("magazine retourné avec succès.")

    def __str__(self):
        
        if self.disponible == True:
            dispo = "Disponible"
        else:
            dispo = "Emprunté"
        return f"Magazine: {self.titre} - Auteur: {self.auteur} - Frequence: {self.frequence} - Statut:[{dispo}]"



class Adherant:
    def __init__(self,nom):
        self.nom = nom
        self.listeEmprunts = []  

    def __str__(self):
        
        return f"Adherent: {self.nom}"   
    

class Bibliothecaire:
   
    def __init__(self):
        self.catalogues = []
        self.liste_adherants = []
    
    def ajouter_document(self, doc):
        """Permet d'ajouter un document dans la liste des catalogues"""
        self.catalogues.append(doc)
        print(f"{doc.titre} ajouté avec succes")

    def InscrireMembre(self,nom):
        """Permet d'inscrire un membre en tant qu'adherant de notre bibliotheque en l'ajoutant dans la liste"""
        adherant= Adherant(nom)

        self.liste_adherants.append(adherant)
        print("Membre ajoute")


    def Lister_document(self):
        """Permet de lister tout notre catalogue"""
        if self.catalogues==[]:
            print("La liste est vide")
        else:
            for doc in self.catalogues:
                print(doc)  

    def Lister_Emprunt(self,nom_adherant):
        """Permet d'afficher la liste des emprunts d'un adhérant"""
        adherant_trouver=None
        if self.liste_adherants==[]:
            print("la liste est vide")
        else:
            for adherant in self.liste_adherants:
                if adherant.nom == nom_adherant:
                    adherant_trouver = adherant
                    
            if not adherant_trouver.listeEmprunts:
                print("Aucun n'emprunt")

            for i in adherant_trouver.listeEmprunts:
                print(i)       

        
    def Lister_membres(self):
        """Permet de lister les adherants de la bibliotheque"""
        if self.liste_adherants==[]:
            print("La liste des membres est vide")
        else:
            for membre in self.liste_adherants:
                print(membre)                

    
    def valider_pret(self, nom_membre, titre_document):
        """Permet de valider un emprunt d'un document"""

        document_trouvee = None
        for document in self.catalogues:
            if document.titre==titre_document:
                document_trouvee = document

        if not document_trouvee :
            print("Document introuvable")       
            return      

        membre_trouvee = None
        for m in self.liste_adherants:
            if m.nom == nom_membre:
                membre_trouvee =  m

        if not membre_trouvee :
            print("Membre introuvable")       
            return
        
        document_trouvee.emprunter()

        membre_trouvee.listeEmprunts.append(document_trouvee)

    def confirmerRetour(self,titre):
        """Permet de confimer le retour d'un document"""
        document_trouvee= None
        

        for doc in self.catalogues:
            if doc.titre == titre:
                document_trouvee= doc
            
        if not document_trouvee :
            print("Document introuvable")       
            return
        
        document_trouvee.retourner()    
            
        
class Menu:
    def __init__(self):
        self.bibliotheque = Bibliothecaire()

    def executer(self):

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

             
menu=Menu()
menu.executer()

    

        


                
                

                
            

        



