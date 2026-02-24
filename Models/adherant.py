class Adherant:
    def __init__(self,nom):
        self.nom = nom
        self.listeEmprunts = []  

    def __str__(self):
        
        return f"Adherent: {self.nom}"