from Models.adherant import Adherant

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