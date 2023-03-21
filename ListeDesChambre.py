import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import requests

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Liste des chambres")

        # Création d'une grille pour afficher les données
        self.grid = Gtk.Grid()
        self.add(self.grid)

        # Création des étiquettes pour les en-têtes de colonnes
        id_chambre_label = Gtk.Label(label="id_chambre")
        self.grid.attach(id_chambre_label, 0, 0, 1, 1)

        numero_chambre_label = Gtk.Label(label="numero_chambre")
        self.grid.attach(numero_chambre_label, 1, 0, 1, 1)

        etage_label = Gtk.Label(label="etage")
        self.grid.attach(etage_label, 2, 0, 1, 1)

        categorie_chambre_label = Gtk.Label(label="categorie_chambre")
        self.grid.attach(categorie_chambre_label, 3, 0, 1, 1)

        prix_chambre_label = Gtk.Label(label="prix_chambre")
        self.grid.attach(prix_chambre_label, 4, 0, 1, 1)

        id_reservation_label = Gtk.Label(label="id_reservation")
        self.grid.attach(id_reservation_label, 5, 0, 1, 1)

        # Appel de l'API pour récupérer les données
        response = requests.get("https://example.com/api/chambres")
        chambres = response.json()

        # Parcours des données pour les afficher dans la grille
        for i, chambre in enumerate(chambres):
            id_chambre = Gtk.Label(label=str(chambre['id_chambre']))
            self.grid.attach(id_chambre, 0, i+1, 1, 1)

            numero_chambre = Gtk.Label(label=str(chambre['numero_chambre']))
            self.grid.attach(numero_chambre, 1, i+1, 1, 1)

            etage = Gtk.Label(label=str(chambre['etage']))
            self.grid.attach(etage, 2, i+1, 1, 1)

            categorie_chambre = Gtk.Label(label=str(chambre['categorie_chambre']))
            self.grid.attach(categorie_chambre, 3, i+1, 1, 1)

            prix_chambre = Gtk.Label(label=str(chambre['prix_chambre']))
            self.grid.attach(prix_chambre, 4, i+1, 1, 1)

            id_reservation = Gtk.Label(label=str(chambre['id_reservation']))
            self.grid.attach(id_reservation, 5, i+1, 1, 1)

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
