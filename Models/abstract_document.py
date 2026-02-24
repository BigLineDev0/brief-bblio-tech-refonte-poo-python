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