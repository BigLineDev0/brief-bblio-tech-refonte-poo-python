class Livre:
    def __init__(self,titre,auteur,disponible=True):
        self.titre = titre
        self.auteur = auteur
        self.disponible = disponible
        
    def __str__(self):
        # dispo = "Disponible" if self.disponible else "Emprunté"
        if self.disponible == True:
            dispo = "Disponible"
        else:
            dispo = "Emprunté"
        return f"Livre: {self.titre} - Auteur: {self.auteur} - Statut:[{dispo}]"
    


class Adherant:
    def __init__(self,nom):
        self.nom = nom
        self.listeEmprunts = []  

    def __str__(self):
        
        return f"Adherent: {self.nom}"   
    

class Bibliothecaire:
    def __init__(self):
        self. liste_livres = []
        self.liste_adherants = []
    
    def ajouter_livre(self, titre, auteur):
        livre = Livre(titre, auteur)

        self.liste_livres.append(livre)
        print("Livre ajouter avec succes")


    def InscrireMembre(self,nom):
        adherant= Adherant(nom)

        self.liste_adherants.append(adherant)
        print("Membre ajoute")


    def Lister_livres(self):
        if self.liste_livres==[]:
            print("La liste des livres est vide")
        else:
            for livre in self.liste_livres:
                print(livre)  

    def Lister_Emprunt(self,nom_adherant):
        adherant_trouver=None
        if self.liste_adherants==[]:
            print("la liste est vide")
        else:
            for adherant in self.liste_adherants:
                if adherant.nom==nom_adherant:
                    adherant_trouver=adherant
                    
            if not adherant_trouver.listeEmprunts:
                print("Aucun n'emprunt")


            for i in adherant_trouver.listeEmprunts:
                print(i)       

        
    def Lister_membres(self):
        if self.liste_adherants==[]:
            print("La liste des membres est vide")
        else:
            for membre in self.liste_adherants:
                print(membre)                

    def valider_pret(self, nom_membre, titre_livre):

        livre_trouvee = None
        for i in self.liste_livres:
            if i.titre==titre_livre:
                livre_trouvee = i
                print(i)

        membre_trouvee = None
        for m in self.liste_adherants:
            if m.nom == nom_membre:
                membre_trouvee =  m

        if livre_trouvee.disponible == False:
            print("ce livre est deja emprunté")
        else:
            membre_trouvee.listeEmprunts.append(livre_trouvee)
            livre_trouvee.disponible = False
            print("Pret validé avec succès.")
        
class Menu:
    def __init__(self):
        self.bibliotheque = Bibliothecaire()

    def executer(self):

        while True:
            print("\n", "-" * 10, "BIBLIOTHEQUE", "-" * 10)
            print("1: Ajouter livre \n" \
            "2: Afficher livre \n" \
            "3: Inscrire membres \n" \
            "4: Afficher membres \n" \
            "5: Valider pret \n" \
            "6: Afficher les emprunts d'un adherant \n"
            "0: Quitter")

            choix = input("\nEntrez votre choix : ")
            
            match choix:
                case "1":
                    try:
                        titre = input("titre : ")
                        if not titre.isalpha():
                            raise ValueError("le titre doit etre une chaine caractere ")
                        auteur = input("auteur : ")
                        if not auteur.isalpha():
                            raise ValueError("l'auteur doit etre une chaine de caractere")
                        self.bibliotheque.ajouter_livre(titre, auteur)
                    except ValueError as e:
                        print("ERREUR: ",e)
                
                case "2":
                    self.bibliotheque.Lister_livres()

                case '3':
                    try:
                        nom = input("Nom : ")
                        if not nom.isalpha():
                            raise ValueError('NOm invalide')
                        self.bibliotheque.InscrireMembre(nom)
                    except ValueError as e:
                        print("Erreur : ", e)

                case '4':
                    self.bibliotheque.Lister_membres()
                
                case '5':
                    print('------------------Liste des adherants-------------------')
                    self.bibliotheque.Lister_membres()
                    try:
                        
                        nom_membre=input("Nom: ")

                        if not nom_membre.isalpha():

                            raise ValueError("le nnom doit etre une chaine de caractere")
                    except ValueError as e:
                        print("Erreur : ", e)

                    print('------------------Liste des livres-------------------')
                    self.bibliotheque.Lister_livres()
                    try:
                        titre_livre=input("Titre: ")
                        if not titre_livre.isalpha():
                            raise ValueError("le titre doit etre une chaine de cractere")
                        
                        self.bibliotheque.valider_pret(nom_membre,titre_livre)
                    except ValueError as e:
                        print("Erreur : ", e)

                case '6':
                    print('----------------Liste des adherants--------------')
                    self.bibliotheque.Lister_membres()
                    try:
                        nom=input('Nom: ')
                        if not nom.isalpha():
                            raise ValueError("le nom doit etre une chaine de caractere")
                        self.bibliotheque.Lister_Emprunt(nom)
                    except ValueError as e:
                        print("Erreur : ", e)
                        
                case '0':
                    print("BYE")
                    break  

                case _:
                    print("choix invalide")  

             
menu=Menu()
menu.executer()
    

        


                
                

                
            

        



