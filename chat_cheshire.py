from personnage import Personnage
from interface import Humeur

class ChatCheshire(Personnage):
    """
    TODO (PARTIE 4) :
        Créez un attribut de classe privé _compteur_chat initialisé à 0
    """
    
    def __init__(self):
        """
        TODO :
        - (PARTIE 2) Appelez le constructeur de la classe parente Personnage
        - (PARTIE 2) Donnez-lui les valeurs suivantes :
                     nom = "Chat Cheshire"
                     energie = 70
                     humeur = Humeur.MYSTERIEUX
            
        - (PARTIE 4) Incrémentez le compteur de personnages à chaque création
                     d’une instance.
        - (PARTIE 4) S'il y a plus qu'un chat, changer le nom du chat pour 
                     "Chat Cheshire {numéro}" où {numéro} est le numéro de l'instance.
                     (La première ChatCheshire reste "Chat Cheshire")
        """
        pass

    """
    TODO (PARTIE 2) : 
        Redéfinissez la méthode abstraite suivante :
            - Nom : reset
            - Paramètres : aucun
            - Description:  Méthode qui permet de réinitialiser les 
                            attributs energie et energie du personnage à leurs valeurs 
                            par défaut.
            - Retour : None
    """
    
    """
    TODO (PARTIE 2) :
        Redéfinissez la méthode abstraite suivante :
            - Nom : se_presenter
            - Paramètres : aucun
            - Description:  Méthode qui permet de se_presenter() pour afficher une phrase thématique 
                            propre du ChatCheshire.
            - Affichage :   "Je suis {nom}, avec un sourire énigmatique."
            - Retour : None
    """
    
    """
    TODO (PARTIE 2) :
        Ajoutez la méthode d'instance suivante :
            - Nom : disparaitre
            - Paramètres : aucun
            - Description:  Méthode qui permet au ChatCheshire de disparaître.
                            Effets :
                                * change son humeur à Humeur.INVISIBLE
                                * met son énergie à 0
            - Affichage :   "{nom} disparaît dans un sourire... Humeur = {humeur}, Énergie = {energie}."
            - Retour : None
    """ 
    
    """
    TODO (PARTIE 2) :
        Ajoutez la méthode d'instance suivante :
            - Nom : reapparaitre
            - Paramètres : aucun
            - Description:  Méthode qui permet au ChatCheshire de reapparaitre.
                            Effets :
                                * change son humeur à Humeur.MYSTERIEUX
                                * met son énergie à 0
            - Affichage :   "{nom} réapparaît soudainement ! Humeur = {humeur}, Énergie = {energie}."
            - Retour : None
    """ 
