from personnage import Personnage
from interface import Humeur

class ReineDeCoeur(Personnage):
    """
    TODO (PARTIE 4) :
        Créez un attribut de classe privé _compteur_reine initialisé à 0
    """
    
    
    def __init__(self):
        """
        TODO :
        - (PARTIE 2) Appelez le constructeur de la classe parente Personnage
        - (PARTIE 2) Donnez-lui les valeurs suivantes :
                     nom = "Reine de Coeur"
                     energie = 80
                     humeur = Humeur.PRESSE
            
        - (PARTIE 4) Incrémentez le compteur de personnages à chaque création
                     d’une instance.
        - (PARTIE 4) S'il y a plus qu'un chat, changer le nom du chat pour 
                     "Reine de Coeur {numéro}" où {numéro} est le numéro de l'instance.
                     (Le premier ReineDeCoeur reste "Reine de Coeur")
        """
        # (PARTIE 2)
        
        # (PARTIE 4)
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
                            propre  ReineDeCoeur.
            - Affichage :   "Je suis {nom}, toujours fusieuse."
            - Retour : None
    """
    
    """
    TODO (PARTIE 2)
    Ajoutez la méthode d'instance suivante :
        - Nom : crier
        - Paramètres : aucun
        - Description:  Méthode qui permet à la ReineDeCoeur de crier.
                        Effets :
                            * change son humeur à Humeur.FURIEUSE
        - Affichage :   "{nom} crie : 'Qu'on lui coupe la tête !' Humeur = {humeur}."
        - Retour : None 
    """
    
    """
    TODO (PARTIE 2)
    Ajoutez la méthode d'instance suivante :
        - Nom : menacer
        - Paramètres : personnage (Personnage) : Le personnage qui est menacé.
        - Description:  Méthode qui permet à la ReineDeCoeur de menacer un autre personnage.
                        Effets :
                            * change l'humeur du personnage menacé à Humeur.TERRIFIEE
        - Affichage :   "{nom_de_la_reine} menace {nom_du_personnage} ! {nom_du_personnage} est maintenant {humeur_de_personnage}."
        - Retour : None
    """
