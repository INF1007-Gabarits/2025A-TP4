from abc import ABC, abstractmethod

from interface import Humeur

class Personnage(ABC):
    """
    TODO (PARTIE 4) :
        Créez un attribut de classe privé _compteur initialisé à 0
    """
    
    def __init__(self, nom, energie, humeur):
        """
        TODO :
        - (PARTIE 1) Initialisez les attributs nom, energie et humeur à partir des paramètres.
        - (PARTIE 4) Incrémentez le compteur de personnages à chaque création d’une instance.
        
        Args:
            nom (str): Le nom du personnage.
            energie (int): Le niveau d'énergie du personnage (0-100).
            humeur (str): L'humeur actuelle du personnage.
        """
        ###  PARTIE 1  ###
        
        
        ###  PARTIE 4  ###
        

    """
    TODO (PARTIE 1) : 
        Ajoutez la méthode abstraite suivante :
            - Décorateur : @abstractmethod
            - Nom : reset
            - Paramètres : aucun
            - Description:  Cette méthode abstraite qui permet de réinitialiser les 
                            attributs du personnage à leurs valeurs par défaut.
            - Retour : None
    """
    
    
    """
    TODO (PARTIE 1) : 
        Ajoutez la méthode abstraite suivante :
            - Décorateur : @abstractmethod
            - Nom : se_presenter
            - Paramètres : aucun
            - Description:  Cette méthode abstraite doit permet d'afficher une présentation 
                            propre à chaque personnage.
            - Retour : None
    """
    
    """
    TODO (PARTIE 1) : 
        Ajoutez la méthode suivante :
            - Nom : est_fatigue
            - Paramètres : aucun
            - Description:  Retourne True si l’énergie du personnage est inférieure à 20, sinon False.
            - Retour : bool
    """

    """
    TODO (PARTIE 1) : 
        Ajoutez la méthode suivante :
            - Nom : dormir
            - Paramètres : aucun
            - Description:  Remet l’énergie du personnage à 100, change son humeur à Humeur.REPOSE
                            et affiche un message indiquant qu’il a bien dormi.
                            Exemple d'affichage: 
                                "{nom} a bien dormi. Énergie = {energie}, humeur = {humeur}."
            - Retour : None
    """

    def __str__(self):
        """
        TODO (PARTIE 4) :
        - Retournez une phrase présentant le personnage, son énergie et son humeur.
        - Exemple : "Je m'appelle {nom}, j'ai {energie} points d'énergie et je suis {humeur}."
        """
        pass

    def __repr__(self):
        """
        TODO (PARTIE 4) :
        - Fournissez une représentation technique utile pour le débogage.
        - Exemple : Personnage(nom='{nom}', energie={energie}, humeur='{humeur}')
        """
        pass
    
    
    """
     TODO (PARTIE 4) : 
        Ajoutez la méthode statique suivante :
            - Décorateur : @staticmethod
            - Nom : compter_personnages
            - Paramètres : aucun
            - Description:  Retourne le nombre total de personnages créés.
                            Cette méthode est statique car elle ne dépend pas d’une instance particulière.
            - Retour : int
    """
