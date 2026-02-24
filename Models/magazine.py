from Models.abstract_document import Document

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