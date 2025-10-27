from contextlib import redirect_stdout
import io
import unittest
from interface import Humeur
from personnage import Personnage
from alice import Alice
from chapelier_fou import ChapelierFou
from chat_cheshire import ChatCheshire
from reine_de_coeur import ReineDeCoeur
from table_de_the import TableDeThe

"""
class TestPartie1(unittest.TestCase):        
    def test_initialisation(self):
        class PersoTest(Personnage):
            def reset(self): pass
            def se_presenter(self): pass
        
        p1 = PersoTest("Test", 10, Humeur.FOU)

        self.assertEqual(p1.nom, "Test")
        self.assertEqual(p1.energie, 10)
        self.assertEqual(p1.humeur, Humeur.FOU)
        
    def test_est_fatigue_true_false(self):
        class PersoTest(Personnage):
            def reset(self): pass
            def se_presenter(self): pass
        
        p1 = PersoTest("Test", 10, Humeur.FOU)
        p2 = PersoTest("Test2", 50, Humeur.JOYEUX)

        self.assertTrue(p1.est_fatigue())
        self.assertFalse(p2.est_fatigue())
    
    def test_print_dormir(self):
        class PersoTest(Personnage):
            def reset(self): pass
            def se_presenter(self): pass
        p = PersoTest("Alice", 50, Humeur.CURIEUSE)
        
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            p.dormir()
        sortie = buffer.getvalue().strip()

        attendu = "Alice a bien dormi. Énergie = 100, humeur = Humeur.REPOSE."
        self.assertEqual(sortie, attendu)
        self.assertEqual(p.energie, 100)
"""


"""
class TestPartie2(unittest.TestCase):
    def setUp(self):        
        Alice._compteur_alice = 0
        ChapelierFou._compteur_chapelier = 0
        ReineDeCoeur._compteur_reine = 0
        ChatCheshire._compteur_chat = 0

    def test_creation_alice_initialisation(self):
        a = Alice()
        self.assertEqual(a.nom, "Alice")
        self.assertEqual(a.energie, 100)
        self.assertEqual(a.humeur, Humeur.CURIEUSE)
    
    def test_alice_reset(self):
        a = Alice()
        a.energie = 20
        a.humeur = Humeur.COLERIQUE
        a.reset()
        self.assertEqual(a.energie, 100)
        self.assertEqual(a.humeur, Humeur.CURIEUSE)

    def test_se_presenter_affichage_alice(self):
        a = Alice()
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            a.se_presenter()
        sortie = buffer.getvalue().strip()
        attendu = "Je suis Alice, pleine de curiosité."
        self.assertEqual(sortie, attendu)

    def test_boire_potion_affichage_et_etat(self):
        a = Alice()
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            a.boire_potion()
        sortie = buffer.getvalue().strip()
        attendu = "Alice boit une potion magique ! Énergie = 110, humeur = grandie."
        self.assertEqual(sortie, attendu)

        self.assertEqual(a.energie, 110)
        self.assertEqual(a.humeur, Humeur.GRANDIE)
        
    def test_chapelier_initialisation(self):
        c = ChapelierFou()
        self.assertTrue(c.nom.startswith("Chapelier Fou"))
        self.assertEqual(c.energie, 90)
        self.assertEqual(c.humeur, Humeur.FOU)
        
    def test_chapelier_reset(self):
        c = ChapelierFou()
        c.energie = 40
        c.humeur = Humeur.COLERIQUE
        c.reset()
        self.assertEqual(c.energie, 90)
        self.assertEqual(c.humeur, Humeur.FOU)
        
    def test_se_presenter_affichage_chapelier(self):
        c = ChapelierFou()
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            c.se_presenter()
        sortie = buffer.getvalue().strip()
        attendu = "Je suis Chapelier Fou, un peu fou."
        self.assertEqual(sortie, attendu)

    def test_offrir_the_affichage_et_effet(self):
        c = ChapelierFou()
        a = Alice()
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            c.offrir_the(a)
        sortie = buffer.getvalue().strip()
        attendu = (
            "Chapelier Fou offre du thé magique à Alice !"
            "Alice gagne 15 énergie. Énergie = 115."
            "Humeur du Chapelier = généreux."
        )
        self.assertEqual(sortie, attendu)

        self.assertEqual(a.energie, 115)
        self.assertEqual(c.humeur, Humeur.GENEREUX)

    def test_chanter_affichage_et_humeur(self):
        c = ChapelierFou()
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            c.chanter()
        sortie = buffer.getvalue().strip()
        attendu = "Le Chapelier Fou chante une chanson absurde ! Humeur = joyeux."
        self.assertEqual(sortie, attendu)
        self.assertEqual(c.humeur, Humeur.JOYEUX)
        
        
        

    def test_chat_cheshire_initialisation(self):
        chat = ChatCheshire()
        self.assertEqual(chat.nom, "Chat Cheshire")
        self.assertEqual(chat.energie, 70)
        self.assertEqual(chat.humeur, Humeur.MYSTERIEUX)
        
    def test_chat_cheshire_reset(self):
        chat = ChatCheshire()
        chat.energie = 10
        chat.humeur = Humeur.COLERIQUE
        chat.reset()
        self.assertEqual(chat.energie, 70)
        self.assertEqual(chat.humeur, Humeur.MYSTERIEUX)

    def test_chat_cheshire_disparaitre(self):
        chat = ChatCheshire()
        chat.disparaitre()
        self.assertEqual(chat.humeur, Humeur.INVISIBLE)
        self.assertEqual(chat.energie, 0)

    def test_chat_cheshire_reapparaitre(self):
        chat = ChatCheshire()
        chat.disparaitre()
        chat.reapparaitre()
        self.assertEqual(chat.humeur, Humeur.MYSTERIEUX)
        self.assertEqual(chat.energie, 70)
        
    def test_se_presenter_affichage_chat(self):
        c = ChatCheshire()
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            c.se_presenter()
        sortie = buffer.getvalue().strip()
        attendu = "Je suis Chat Cheshire, avec un sourire énigmatique."
        self.assertEqual(sortie, attendu)
        
    def test_disparaitre_affichage_et_etat(self):
        c = ChatCheshire()
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            c.disparaitre()
        sortie = buffer.getvalue().strip()
        attendu = "Chat Cheshire disparaît dans un sourire... Humeur = invisible, Énergie = 0."
        self.assertEqual(sortie, attendu)
        
        self.assertEqual(c.humeur, Humeur.INVISIBLE)
        self.assertEqual(c.energie, 0)
    
    def test_reapparaitre_affichage_et_etat(self):
        c = ChatCheshire()
        c.humeur = Humeur.INVISIBLE
        c.energie = 0
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            c.reapparaitre()
        sortie = buffer.getvalue().strip()
        attendu = "Chat Cheshire réapparaît soudainement ! Humeur = mystérieux, Énergie = 70."
        self.assertEqual(sortie, attendu)

        self.assertEqual(c.humeur, Humeur.MYSTERIEUX)
        self.assertEqual(c.energie, 70)


    def test_reine_initialisation(self):
        r = ReineDeCoeur()
        self.assertEqual(r.nom, "Reine de Coeur")
        self.assertEqual(r.energie, 100)
        self.assertEqual(r.humeur, Humeur.COLERIQUE)
    
    def test_reine_reset(self):
        r = ReineDeCoeur()
        r.energie = 50
        r.humeur = Humeur.JOYEUX
        r.reset()
        self.assertEqual(r.energie, 100)
        self.assertEqual(r.humeur, Humeur.COLERIQUE)
    
    def test_se_presenter_affichage_rein(self):
        r = ReineDeCoeur()
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            r.se_presenter()
        sortie = buffer.getvalue().strip()
        attendu = "Je suis Reine de Coeur, toujours fusieuse."
        self.assertEqual(sortie, attendu)

    def test_crier_affichage_et_humeur(self):
        r = ReineDeCoeur()
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            r.crier()
        sortie = buffer.getvalue().strip()
        attendu = "Reine de Coeur crie : 'Qu'on lui coupe la tête !' Humeur = furieuse."
        self.assertEqual(sortie, attendu)

        self.assertEqual(r.humeur, Humeur.FURIEUSE)
        
    def test_menacer_affichage_et_effet(self):
        r = ReineDeCoeur()
        c = ChatCheshire()  # personnage menacé

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            r.menacer(c)
        sortie = buffer.getvalue().strip()
        attendu = "Reine de Coeur menace Chat Cheshire ! Chat Cheshire est maintenant terrifiée."
        self.assertEqual(sortie, attendu)

        self.assertEqual(c.humeur, Humeur.TERRIFIEE)
"""


"""
class TestPartie3(unittest.TestCase):
    def setUp(self):
        Alice._compteur_alice = 0
        ChapelierFou._compteur_chapelier = 0
        ReineDeCoeur._compteur_reine = 0
        
        self.table = TableDeThe()
        self.alice = Alice()
        self.chapelier = ChapelierFou()
        self.reine = ReineDeCoeur()

    def test_ajouter_personnage(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            self.table.ajouter_personnage(self.alice)
        sortie = buffer.getvalue().strip()
        self.assertIn("Alice rejoint la table du thé.", sortie)
        self.assertIn(self.alice, self.table.personnages)

    def test_ajouter_personnage_deja_present(self):
        self.table.ajouter_personnage(self.alice)
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            self.table.ajouter_personnage(self.alice)
        sortie = buffer.getvalue().strip()
        self.assertIn("Alice est déjà à la table.", sortie)
        self.assertEqual(len(self.table.personnages), 1)

    def test_retirer_personnage(self):
        self.table.ajouter_personnage(self.alice)
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            self.table.retirer_personnage(self.alice)
        sortie = buffer.getvalue().strip()
        self.assertIn("Alice quitte la table du thé.", sortie)
        self.assertNotIn(self.alice, self.table.personnages)
        
    def test_retirer_personnage_absent(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            self.table.retirer_personnage(self.reine)
        sortie = buffer.getvalue().strip()
        self.assertIn("Reine de Coeur n'était pas à la table.", sortie)

    def test_se_presenter_tous(self):
        self.table.ajouter_personnage(self.alice)
        self.table.ajouter_personnage(self.chapelier)
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            self.table.se_presenter_tous()
        sortie = buffer.getvalue().strip()
        self.assertIn("Autour de la table, chacun se présente :", sortie)
        self.assertIn("Alice", sortie)
        self.assertIn("Chapelier Fou", sortie)
    
    def test_energie_totale(self):
        self.table.ajouter_personnage(self.alice)
        self.table.ajouter_personnage(self.chapelier)
        energie_attendue = self.alice.energie + self.chapelier.energie
        self.assertEqual(self.table.energie_totale(), energie_attendue)

    def test_organiser_the_avec_chapelier(self):
        self.table.ajouter_personnage(self.alice)
        self.table.ajouter_personnage(self.chapelier)
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            self.table.organiser_the()
        sortie = buffer.getvalue().strip()
        self.assertIn("Chapelier Fou organise un thé magique !", sortie)
        self.assertIn("Autour de la table, chacun se présente :", sortie)
"""


"""
class TestPartie4(unittest.TestCase):
    def test_compteur_increment(self):
        class PersoTest(Personnage):
            def reset(self): pass
            def se_presenter(self): pass
        
        Personnage._compteur = 0
        _ = PersoTest("Bob", 30, Humeur.JOYEUX)
        _ = Alice()
        self.assertEqual(Personnage.compter_personnages(), 2)

    def test_str(self):
        class PersoTest(Personnage):
            def reset(self): pass
            def se_presenter(self): pass
        p = PersoTest("Alice", 50, Humeur.COLERIQUE)
        texte = str(p)
        attendu = "Je m'appelle Alice, j'ai 50 points d'énergie et je suis colérique."
        self.assertEqual(texte, attendu)

    def test_repr(self):
        class PersoTest(Personnage):
            def reset(self): pass
            def se_presenter(self): pass
        p = PersoTest("Alice", 50, Humeur.COLERIQUE)
        texte = repr(p)
        attendu = "Personnage(nom='Alice', energie=50, humeur='colérique')"
        self.assertEqual(texte, attendu)

    def test_len_(self):
        self.table = TableDeThe()
        self.alice = Alice()
        self.reine = ReineDeCoeur()
        self.table.ajouter_personnage(self.alice)
        self.table.ajouter_personnage(self.reine)
        self.assertEqual(len(self.table), 2)
        
    def test_incrementation_nom_alice(self):
        Alice._compteur_alice = 0
        a1 = Alice()
        a2 = Alice()
        a3 = Alice()
        self.assertEqual(a1.nom, "Alice")
        self.assertEqual(a2.nom, "Alice 2")
        self.assertEqual(a3.nom, "Alice 3")
        
    def test_incrementation_nom_chaplier(self):
        ChapelierFou._compteur_chapelier = 0
        c1 = ChapelierFou()
        c2 = ChapelierFou()
        c3 = ChapelierFou()
        self.assertEqual(c1.nom, "Chapelier Fou")
        self.assertEqual(c2.nom, "Chapelier Fou 2")
        self.assertEqual(c3.nom, "Chapelier Fou 3")
        
    def test_incrementation_nom_chat(self):
        ChatCheshire._compteur_chat = 0
        c1 = ChatCheshire()
        c2 = ChatCheshire()
        c3 = ChatCheshire()
        self.assertEqual(c1.nom, "Chat Cheshire")
        self.assertEqual(c2.nom, "Chat Cheshire 2")
        self.assertEqual(c3.nom, "Chat Cheshire 3")
        
    def test_incrementation_nom_rein(self):
        ReineDeCoeur._compteur_reine = 0
        r1 = ReineDeCoeur()
        r2 = ReineDeCoeur()
        r3 = ReineDeCoeur()
        self.assertEqual(r1.nom, "Reine de Coeur")
        self.assertEqual(r2.nom, "Reine de Coeur 2")
        self.assertEqual(r3.nom, "Reine de Coeur 3")
        
    def test_len(self):
        self.table = TableDeThe()
        self.alice = Alice()
        self.chapelier = ChapelierFou()
        self.reine = ReineDeCoeur()
        
        self.table.ajouter_personnage(self.alice)
        self.table.ajouter_personnage(self.reine)
        self.assertEqual(len(self.table), 2)
"""
if __name__ == "__main__":
    unittest.main()
