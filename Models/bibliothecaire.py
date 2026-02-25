from Models.adherant import Adherant
from Models.database import maconnexion
class Bibliothecaire:
   
    def __init__(self):
        self.catalogues = []
        self.liste_adherants = []
    
    def ajouter_Magazine(self, doc):
        """Permet d'ajouter un document dans la liste des catalogues"""
        try:
            cursor = maconnexion.cursor()
            query="insert into catalogues(titre,auteur,type,frequence) values(%s,%s,%s,%s)"
            cursor.execute(query,(doc.titre, doc.auteur, doc.type_doc, doc.frequence))
            maconnexion.commit()
            print(f"{doc.titre} ajouté avec succes")

        except Exception as e:
            print("Erreur.", e)
        
        cursor.close()
        

    def ajouter_Livre(self, doc):
        """Permet d'ajouter un document dans la liste des catalogues"""
        try:
            cursor=maconnexion.cursor()
            query=" insert into catalogues(titre,auteur,type) values(%s,%s,%s)"
            cursor.execute(query,(doc.titre,doc.auteur,doc.type_doc))
            maconnexion.commit()
            print(f"{doc.titre} ajouté avec succes")

        except Exception as e:
            print("Erreur.", e)
        
        cursor.close()

    def InscrireMembre(self, i: Adherant): # la variable i est type objet
        """Permet d'inscrire un membre en tant qu'adherant de notre bibliotheque en l'ajoutant dans la liste"""
        try:
            cursor=maconnexion.cursor()
            query="insert into adherants(nom) values(%s)"
            cursor.execute(query,(i,))
            maconnexion.commit()

            print("Membre ajoute ")
            
        except Exception as e:
            print("Erreur.", e)
        
        cursor.close()

    def Lister_document(self):
        """Permet de lister tout notre catalogue"""
       
        try:
            cursor=maconnexion.cursor()
            query="select * from catalogues"
            cursor.execute(query)
            liste_catalogue=cursor.fetchall()
            
            if not liste_catalogue:
                print("la liste est vide")
            else:
               for i in liste_catalogue:
                   
                   print(i)   
            
        
        except Exception as e:
            print("Erreur.", e)
        
        cursor.close()
            

         
    def Lister_Emprunt(self,id_adherant):
        """Permet d'afficher la liste des emprunts d'un adhérant"""

        cursor=maconnexion.cursor()
        query="""
        SELECT a.nom , c.titre, e.date_emprunt, e.date_retour_programme from adherants as a 
        join emprunts as e on e.id_adherant=a.id 
        join catalogues as c on e.id_catalogue=c.id where a.id=%s
        """
        cursor.execute(query,(id_adherant,))
        adherant=cursor.fetchall()
        if not adherant :
            print("La liste est vide")
     
        else:
            for i in adherant:
                print(i)
        
    def Lister_membres(self):
        """Permet de lister les adherants de la bibliotheque"""
        try:
            cursor=maconnexion.cursor()
            query="select * from adherants"
            cursor.execute(query)
            liste_membres=cursor.fetchall()
            
            if not liste_membres:
                print("la liste est vide")
            else:
               for i in liste_membres:
                   
                    print(i)   
            
        
        except Exception as e:
            print("Erreur.", e)
        
        cursor.close()             

    
    def valider_pret(self, id_membre, id_document,date_retour_programme):
        """Permet de valider un emprunt d'un document"""
        

        try:
            cursor=maconnexion.cursor()
            query="select * from catalogues where id=%s"
            cursor.execute(query,(id_document,))
            document=cursor.fetchone()
            
            if not document:
                print("Le document est introuvable")
           
            query="select * from adherants where id= %s"
            cursor.execute(query,(id_membre,))  
            membre=cursor.fetchone()  
            if not membre:
                print("Ce membre est introuvable")

            cursor.execute("SELECT * FROM emprunts WHERE status = 'Emprunte'")

            if cursor.fetchone():
                print("Ce document est deja emprunté.")
                return
            else: 
                query="insert into emprunts(id_adherant,id_catalogue,date_retour_programme) values(%s,%s,%s)"
                cursor.execute(query,(id_membre,id_document,date_retour_programme))
                maconnexion.commit()
                print("L'emprunt est valide avec succes")

        except Exception as e:
            print("Erreur.", e)
        
        cursor.close()


       

    def confirmerRetour(self,id_membre, id_document):
        """Permet de confimer le retour d'un document"""

        try:

            cursor=maconnexion.cursor()
            cursor.execute("select * from adherants where id=%s", (id_membre,))
            adherant=cursor.fetchone()

            if not adherant:
                print("Le membre n'est pas trouve")

            cursor.execute("select * from catalogues where id=%s", (id_document,))    
            document=cursor.fetchone()

            if not document:
                print("Le document est introuvable")

            query="""
            update emprunts set date_retour = NOW(), status='Restitue' 
            where id_catalogue=%s and id_adherant=%s
            """ 
            cursor.execute(query,(id_membre,id_document))
            maconnexion.commit()
            print("Le document est rendu avec succes ")
        except Exception as e:
            print("Erreur.", e)
        
        cursor.close()
    





