from personnage import Personnage
from chapelier_fou import ChapelierFou

class TableDeThe:
    def __init__(self):
        """
        Initialise une nouvelle table de thé.
        
        TODO (PARTIE 2):
            - Créer un attribut d’instance `personnages` initialisé à une liste vide.
        """
        pass

    def ajouter_personnage(self, personnage: Personnage):
        """
        Ajoute un personnage à la table du thé.
        
        Args:
            personnage (Personnage): Le personnage à ajouter.

        TODO (PARTIE 2):
            - Vérifier si le personnage n’est pas déjà dans la liste `personnages`.
            - Si non, 
                    1. l’ajouter à la liste des personnage et 
                    2. afficher: "{nom} rejoint la table du thé."
            - Sinon, afficher: "{nom} est déjà à la table."
        """
        pass

    def retirer_personnage(self, personnage: Personnage):
        """
        Retire un personnage de la table du thé.
        
        Args:
            personnage (Personnage): Le personnage à retirer.

        TODO (PARTIE 2):
            - Vérifier si le personnage est dans la liste `personnages`.
            - Si oui, 
                1. le retirer 
                2. afficher: "{nom} quitte la table du thé."
            - Sinon, afficher: "{nom} n'était pas à la table."
        """
        pass

    def se_presenter_tous(self):
        """
        Fait se présenter tous les personnages autour de la table.
        
        TODO (PARTIE 2):
            - Afficher: "Autour de la table, chacun se présente :"
            - Appeler la méthode `se_presenter()` pour chaque personnage dans `personnages`.
        """
        pass

    def energie_totale(self):
        """
        Calcule l’énergie totale des personnages présents à la table.
        
        Returns:
            int: La somme des énergies de tous les personnages.

        TODO (PARTIE 2):
            - Retourner la somme des énergies (`p.energie`) pour chaque personnage de `personnages`.
        """
        pass

    def organiser_the(self):
        """
        Organise un thé magique dirigé par le Chapelier Fou.
        
        TODO (PARTIE 2):
            - Rechercher les personnages de type `ChapelierFou` dans `personnages`.
            - Si aucun trouvé, 
                1. afficher: "Il n’y a pas de Chapelier Fou pour organiser le thé."
            - Sinon, 
                1. afficher: "{nom} organise un thé magique !"
                2. Pour chaque autre personnage, appeler `chapelier.offrir_the(p)`.
                3. Enfin, appeler `self.se_presenter_tous()` pour que tout le monde se présente.
        """
        pass
        
    def __len__(self):
        """
        Retourne le nombre de personnages présents à la table.

        Returns:
            int: Le nombre de personnages.

        TODO (PARTIE 4):
            - Retourner la longueur de la liste `personnages` avec `len()`.
        """
        pass
