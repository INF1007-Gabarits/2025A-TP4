import random
from alice import Alice
from aventure import Aventure
from chapelier_fou import ChapelierFou
from chat_cheshire import ChatCheshire
from personnage import Personnage
from reine_de_coeur import ReineDeCoeur
from table_de_the import TableDeThe



if __name__ == "__main__":
    """
    PARTIE 2 : Heritage et Polymorphisme
    A Faire: 
        1. Créez les objets représentant chaque personnage 
            (Alice, ChapelierFou, ReineDeCoeur, ChatCheshire)
        
        2. Regroupez tous les personnages dans une liste
        3. Ajouter 5 personnages supplémentaires alétoires à la liste (utilisez random.choice)

    """
    
    # TODO (PARTIE 2):
    
    # END TODO
    
    
    """
    PARTIE 3 : Composition
    
    A Faire: 
        1. Créez une instance de TableDeThe
        2. Ajoutez-y les 5 personnages créés précédemment
        3. Essayez d’ajouter le Chapelier une seconde fois pour tester la gestion des doublons
        
        4. Affichez le nombre de personnages à la table (utilisez la méthode __len__())
            Exemple de sortie attendue :
            Nombre de personnages à la table : 5
            
        5. Affichez l’énergie totale des personnages à la table (utilisez la méthode energie_totale())
            Exemple de sortie attendue :
            Energie totale à la table : 430
            
        6. Faites organiser le thé par le Chapelier (utilisez la méthode organiser_the())   
    
    """
    # TODO (PARTIE 3):
    
    # END TODO
    
    """
    PARTIE 4 : Élément statique et built-in
    
    A Faire: 
        1. Affichez le nombre total de personnages créés en utilisant la méthode statique compter_personnages()
                Exemple de sortie attendue :
                Nombre total de personnages créés : X
            
        2. Affichez les détails de chaque personnage en utilisant la méthode __str__()
                Exemple de sortie attendue :
                Présentation des personnages :
                Je m'appelle Alice, j'ai 100 points d'énergie et je suis curieuse.
                ...
    
    """
    # TODO (PARTIE 4):
    
    # END TODO

    
    """
    PARTIE 5 : Simulation de l’aventure (BONUS)
    À Faire: 
        1. Suivez le TODO
    """
    # TODO: Créez un objet Aventure en lui passant la liste des personnages

    # END TODO
        
    print("=== Début de l’Aventure au Pays des Merveilles ===\n")
    print("Voici les personnages qui vont participer à cette aventure :") 
    
    # TODO: Presenter les personnage de l'aventure

    # END TODO
    print()

    print("=== Le Thé du Chapelier ===")
    # TODO: Appelez la methode the_du_chapelier de l'objet aventure

    # END TODO
    print()
    
    print("=== La Colère de la Reine de Coeur ===")
    # TODO: Appelez la methode dispute_royale de l'objet aventure

    # END TODO
    print()
    
    print("=== Le Mystère du Chat Cheshire ===")
    # TODO: Appelez la methode mystere_du_chat de l'objet aventure

    # END TODO
    print()
    
    print("=== Conclusion ===")
    # TODO: Appelez la methode statistique de l'objet aventure

    # END TODO
    print()
    
    print("=== Fin de l’Aventure ===")
