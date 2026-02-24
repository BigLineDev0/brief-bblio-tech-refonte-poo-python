## Biblio-Tech - Refonte
# Projet réalisé en binôme par :
- Adji Sambe
- Aliou Diallo

# Objectif du projet
Ce projet consiste à industrialiser un système de gestion de bibliothèque en appliquant les principes de la Programmation Orientée Objet (POO).
Initialement conçu uniquement pour gérer des Livres, le système a été généralisé afin de pouvoir manipuler tout type de Document (Livre, Magazine, etc.) sans modifier le code du gestionnaire principal (Bibliothécaire).
L’objectif est de rendre le système : Évolutif,  Sécurisé, Modulaire et Conforme aux principes d’encapsulation, d’abstraction et de polymorphisme
Le projet est découpé en plusieurs modules afin d’assurer une bonne organisation et une meilleure maintenabilité :

-   document.py
-   livre.py
-   magazine.py
-   adherant.py
-   bibliothecaire.py
-   main.py

# document.py

    Contient la classe abstraite Document.
    Définit la structure commune obligatoire à tous les supports.
    Empêche l’instanciation directe d’un document générique.
    Contient les méthodes abstraites emprunter() et retourner().

# livre.py
    Classe Livre héritant de Document.
    Implémente ses propres règles d’emprunt et de retour.
    magazine.py
    Classe Magazine héritant de Document.
    Ajoute l’attribut frequence.
    Implémente ses propres méthodes d’emprunt et de retour.

# adherant.py
    Classe Adherant.
    Gère les informations des membres.
    Stocke la liste des emprunts.
    bibliothecaire.py
    Classe Bibliothecaire.
    Gère le catalogue.
    Gère les membres.
    Valide les prêts et retours.
    Fonctionne de manière polymorphique sans connaître le type précis du document.

# main.py
    Interface console utilisant match/case.
    Permet l’interaction utilisateur.
    Gère les erreurs.
    Recherche les documents par titre uniquement.


# Classe Abstraite
    La classe Document hérite de ABC et impose :
    @abstractmethod
    def emprunter(self):

    @abstractmethod
        def retourner(self):
        

Cela garantit que chaque type de document définit son propre comportement.
Un document générique ne peut pas exister.

# Encapsulation (Verrouillage des données)
    L’attribut __disponible est privé :
    self.__disponible

Il ne peut pas être modifié directement depuis l’extérieur.
Seules les méthodes internes emprunter() et retourner() peuvent changer son état.
Cela empêche toute modification sauvage du type :
document.__disponible = False  

# Polymorphisme
Le Bibliothecaire manipule les documents sans savoir s’il s’agit d’un Livre ou d’un Magazine :
document_trouvee.emprunter()

Chaque objet applique sa propre logique automatiquement.
Cela rend le système évolutif.

# Fonctionnalités
- Ajouter un magazine
- Ajouter un livre
- Afficher le catalogue
- Inscrire un membre
- Afficher les membres
- Valider un prêt
- Afficher les emprunts d’un adhérant
- Confirmer un retour
- Recherche par titre obligatoire
- Gestion explicite des erreurs
- Blocage d’emprunt si document indisponible
- Le document est introuvable
- Le membre est introuvable
- Le document est déjà emprunté
- Tentative de retour d’un document non emprunté
- Saisie invalide

# Lancement du programme
Exécuter le fichier :
python main.py

Le menu interactif s’affiche et guide l’utilisateur.

