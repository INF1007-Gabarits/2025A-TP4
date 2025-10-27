### **Barème global du TP ( /25 + 1 bonus)**

| **Catégorie**        | **Critère**              | **Points**  |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- |
| **Classe abstraite `Personnage`**             | Initialisation des attributs `nom`, `energie`, `humeur` dans `__init__()`  | 1.0  |
|    | Méthodes abstraites `reset()` et `se_presenter()` présentes avec `@abstractmethod` et respect des consignes          | 1.0  |
|    | Méthodes de base : `est_fatigue()` retourne un booléen correct et `dormir()` remet énergie à 100, humeur à `Humeur.REPOSE`  | 1.0  |
|    | Attribut de classe `_compteur` initialisé à 0, incrémenté à chaque instance, méthode statique `compter_personnages()` fonctionnelle           | 1.0  |
|    | Méthodes `__str__()` et `__repr__()` cohérentes et descriptives            | 1.0  |
| **→ Total Personnage**      |        | **5.0**     |
| **Héritage et spécialisation**                | Constructeurs des sous-classes (`Alice`, `ChapelierFou`, `ChatCheshire`, `ReineDeCoeur`) appellent correctement `super().__init__()` avec les bonnes valeurs           | 1.0  |
|    | Méthode `reset()` redéfinie dans chaque sous-classe avec réinitialisation correcte des attributs   | 1.0  |
|    | Méthode `se_presenter()` redéfinie avec un message thématique propre à chaque personnage           | 1.0  |
|    | Méthodes spécifiques fonctionnelles : <br>• `boire_potion()` (Alice) <br>• `offrir_the()`, `chanter()` (ChapelierFou) <br>• `disparaitre()`, `reapparaitre()` (ChatCheshire) <br>• `crier()`, `menacer()` (ReineDeCoeur) | 1.5  |
|    | Cohérence générale du code et respect du style objet     | 0.5  |
| **→ Total Héritage**        |        | **5.0**     |
| **Composition : `TableDeThe`**                | Attribut `personnages` bien initialisé dans `__init__()`                   | 0.5  |
|    | `ajouter_personnage()` et `retirer_personnage()` gèrent correctement les ajouts, retraits, doublons et affichages           | 1.0  |
|    | `se_presenter_tous()` affiche l’en-tête et appelle `se_presenter()` sur chaque personnage          | 0.5  |
|    | `energie_totale()` retourne la somme correcte des énergies des personnages                  | 0.5  |
|    | `organiser_the()` : recherche des Chapeliers, message si absent, appels à `offrir_the()` et `se_presenter_tous()`           | 1.5  |
| **→ Total TableDeThe**      |        | **4.0**     |
| **Attributs de classe et méthodes statiques** | Implémentation correcte de `__len__()` retournant le nombre de personnages                  | 0.5  |
|    | Affichages cohérents dans toutes les méthodes (`ajouter_personnage`, `retirer_personnage`, `organiser_the`, etc.)           | 0.5  |
|    | Bonne gestion des compteurs d’instances multiples : noms numérotés et suivi correct                | 2.0  |
|    | Cohérence d’ensemble : intégration correcte entre `organiser_the()`, `offrir_the()`, `se_presenter_tous()`, compteurs et énergies             | 2.0  |
| **→ Total Attributs / Méthodes statiques**    |        | **5.0**     |
| **Implémentation du `main`**                  | Création correcte des objets principaux et ajout aléatoire de 5 personnages                 | 0.5  |
|    | Création de `TableDeThe`, gestion des doublons, affichage de `__len__()` et `energie_totale()`, organisation du thé         | 1.0  |
|    | Affichage du nombre total via `compter_personnages()` et présentation via `__str__()`              | 0.5  |
|    | Création de `Aventure`, exécution de `the_du_chapelier()`, `dispute_royale()`, `mystere_du_chat()`, `statistique()`         | 1.0  |
| **→ Total main**     |        | **3.0**     |
| **Qualité du code**  | Lisibilité, cohérence, respect du style Python, modularité, bonnes pratiques POO            | **2.5**     |
| **Simulation de l’aventure : `Aventure`**     | Fonctionnalité complète et dynamique de la simulation (bonus)              | **+1.0**    |
| **→ Total global**   |        | **25 points + 1 point bonus** |


