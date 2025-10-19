import random
from table_de_the import TableDeThe
from alice import Alice
from chapelier_fou import ChapelierFou
from reine_de_coeur import ReineDeCoeur
from chat_cheshire import ChatCheshire

# PARTIE 5 : Simulation de l’aventure    
class Aventure:
    def __init__(self, personnages):
        """
        Initialise une nouvelle aventure avec les personnages fournis.
        
        Args:
            personnages (list[Personnage]): Liste des personnages présents dans l’aventure.
        
        TODO:
            - Créer une instance de TableDeThe et la stocker dans l’attribut `self.table`.
            - Stocker la liste de personnages dans `self.personnages`.
        """
        pass
        

    def the_du_chapelier(self):
        """
        Simule la scène du thé du Chapelier Fou.
        
        TODO:
            - Trouver le personnage de type `ChapelierFou` dans `self.personnages`.
            - Si trouvé :
                1. Afficher "Un Chapelier Fou organise un thé. Voyons qui vient !"
                2. Ajouter le Chapelier à la table.
                3. Inviter aléatoirement d’autres personnages (au moins 2 en tout).
                4. Appeler `self.table.organiser_the()` pour que le Chapelier offre du thé.
                5. Faire chanter le Chapelier via `chapelier.chanter()`.
            - Sinon, afficher "Il n’y a pas de Chapelier Fou pour organiser le thé."
        """
        pass
        chapelier = next((p for p in self.personnages if isinstance(p, ChapelierFou)), None)

            
    def dispute_royale(self):
        """
        Simule une dispute entre la Reine de Cœur et un autre personnage choisi au hasard.
        
        TODO:
            - Trouver la Reine de Cœur (`ReineDeCoeur`) dans `self.personnages`.
            - Choisir aléatoirement une victime différente de la reine.
            - Si la reine et une victime existent :
                - Faire crier la reine (`reine.crier()`) et menacer la victime (`reine.menacer(victime)`).
                - Gérer les cas particuliers selon le type de la victime :
                    * Alice : afficher un message et appeler `boire_potion()`
                    * ChatCheshire : afficher un message, puis appeler `disparaitre()` et `reapparaitre()`
            - Sinon, afficher "Il n’y a pas de Reine de Coeur ou un autre personnage dans cette aventure."
        """
        pass
        reine = next((p for p in self.personnages if isinstance(p, ReineDeCoeur)), None)
        victime = None

            
    def mystere_du_chat(self):
        """
        Met en scène le mystère du Chat Cheshire.
        
        TODO:
            - Trouver le Chat Cheshire dans `self.personnages`.
            - S’il existe :
                - Le faire disparaître (`disparaitre()`), afficher le mystère, puis le faire réapparaître.
            - Sinon, afficher "Il n’y a pas de Chat Cheshire dans cette aventure."
        """
        pass
        chat = next((p for p in self.personnages if isinstance(p, ChatCheshire)), None)


    def presentation_personnages(self):
        """
        Fait se présenter tous les personnages de l’aventure.
        
        TODO:
            - Parcourir `self.personnages` et appeler `se_presenter()` pour chacun.
        """
        pass
        
    def statistique(self):
        """
        Affiche les statistiques finales de l’aventure.
        
        TODO:
            - Pour chaque personnage, afficher sa représentation (`repr(p)`).
            - Afficher l’énergie totale autour de la table (`self.table.energie_totale()`).
            - Afficher le nombre total de personnages créés (`compter_personnages()`).
            - Afficher une phrase de conclusion : "Le Pays des Merveilles retrouve enfin un peu de calme..."
        """
        pass
