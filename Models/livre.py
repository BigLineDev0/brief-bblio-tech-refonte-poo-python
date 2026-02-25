from Models.abstract_document import Document

class Livre(Document):
    def __init__(self, titre, auteur, type_doc, disponible=True):
        super().__init__(titre, auteur, type_doc, disponible)
    
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