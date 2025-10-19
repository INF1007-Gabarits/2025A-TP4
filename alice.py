from personnage import Personnage

class Alice(Personnage):
    """
    TODO (PARTIE 4) :
        Créez un attribut de classe privé _compteur_alice initialisé à 0
    """
    
    
    def __init__(self):
        """
        TODO :
        - (PARTIE 2) Appelez le constructeur de la classe parente Personnage
        - (PARTIE 2) Donnez-lui les valeurs suivantes :
                     nom = "Alice"
                     energie = 100
                     humeur = Humeur.CURIEUSE
            
        - (PARTIE 4) Incrémentez le compteur de personnages à chaque création
                     d’une instance.
        - (PARTIE 4) S'il y a plus qu'une alice, changer le nom d'Alice pour 
                     "Alice {numéro}" où {numéro} est le numéro de l'instance.
                     (La première Alice reste "Alice", la deuxième devient "Alice 2", etc.)
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
                            propre à Alice.
            - Affichage :   "Je suis {nom}, pleine de curiosité."
            - Retour : None
    """
    
    """
    TODO (PARTIE 2) :
        Ajoutez la méthode d'instance suivante :
            - Nom : boire_potion
            - Paramètres : aucun
            - Description:  Méthode qui permet à Alice de boire une potion magique.
                            Effets :
                                * augmente son énergie de 10
                                * change son humeur à "grandie"
            - Affichage :   "{nom} boit une potion magique ! Énergie = {energie}, humeur = {humeur}."
            - Retour : None
    """
