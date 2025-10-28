from personnage import Personnage
from interface import Humeur


class ChapelierFou(Personnage):
    """
    TODO (PARTIE 4) :
        Créez un attribut de classe privé _compteur_chapelier initialisé à 0
    """
    
    def __init__(self):
        """
        TODO :
        - (PARTIE 2) Appelez le constructeur de la classe parente Personnage
        - (PARTIE 2) Donnez-lui les valeurs suivantes :
                     nom = "Chapelier Fou"
                     energie = 90
                     humeur = Humeur.FOU
            
        - (PARTIE 4) Incrémentez le compteur de personnages à chaque création
                     d’une instance.
        - (PARTIE 4) S'il y a plus qu'une chapelier fou, changer le nom du chapelier pour 
                     "Chapelier Fou {numéro}" où {numéro} est le numéro de l'instance.
                     (La première ChapelierFou reste "Chapelier Fou", la deuxième devient "Chapelier Fou 2", etc.)
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
                            propre au Chapelier Fou.
            - Affichage :   "Je suis {nom}, un peu fou."
            - Retour : None
    """
    
    """
    TODO (PARTIE 2) :
        Ajoutez la méthode d'instance suivante :
            - Nom : offrir_the
            - Paramètres : autre_personnage (Personnage) : Le personnage qui reçoit le thé.
            - Description:  Méthode qui permet au Chapelier Fou d'offrir du thé magique à un autre personnage.
                            Cette action augmente l'énergie de l'autre personnage de 15 points
                            et change l'humeur du Chapelier Fou à Humeur.GENEREUX.
            - Affichage :   "{nom_du_chapelier} offre du thé magique à {nom_de_l_autre_personnage} ! 
                             {nom_de_l_autre_personnage} gagne 15 énergie. Énergie = {nouvelle_energie_de_l_autre_personnage}. 
                             Humeur du Chapelier = généreux."
            - Retour : None
    """
    
    """
    TODO (PARTIE 2) :
        Ajoutez la méthode d'instance suivante :
            - Nom : chanter
            - Paramètres : aucun
            - Description:  Méthode qui permet au Chapelier Fou de chanter une chanson absurde.
                            Cette action change son humeur à Humeur.JOYEUX.
            - Affichage :   "Le Chapelier Fou chante une chanson absurde ! Humeur = {humeur}."
            - Retour : None
    """
  