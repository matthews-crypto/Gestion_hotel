import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import requests

class ReservationForm(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Formulaire de réservation")
        self.set_default_size(400, 300)

        # Créer une grille pour organiser les widgets
        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)
        self.add(grid)

        # Champ de saisie pour le nom
        label_nom = Gtk.Label(label="Nom")
        grid.attach(label_nom, 0, 0, 1, 1)
        entry_nom = Gtk.Entry()
        entry_nom.set_placeholder_text("Nom")
        grid.attach(entry_nom, 1, 0, 1, 1)

        # Champ de saisie pour le prénom
        label_prenom = Gtk.Label(label="Prénom")
        grid.attach(label_prenom, 0, 1, 1, 1)
        entry_prenom = Gtk.Entry()
        entry_prenom.set_placeholder_text("Prénom")
        grid.attach(entry_prenom, 1, 1, 1, 1)

        # Champ de saisie pour le numéro de téléphone
        label_telephone = Gtk.Label(label="Téléphone")
        grid.attach(label_telephone, 0, 2, 1, 1)
        entry_telephone = Gtk.Entry()
        entry_telephone.set_placeholder_text("Numéro de téléphone")
        grid.attach(entry_telephone, 1, 2, 1, 1)

        # Champ de saisie pour le numéro de chambre
        label_chambre = Gtk.Label(label="Numéro de chambre")
        grid.attach(label_chambre, 0, 3, 1, 1)
        entry_chambre = Gtk.Entry()
        entry_chambre.set_placeholder_text("Numéro de chambre")
        grid.attach(entry_chambre, 1, 3, 1, 1)

        # Champ de saisie pour la date d'entrée
        label_date_entree = Gtk.Label(label="Date d'entrée")
        grid.attach(label_date_entree, 0, 4, 1, 1)
        entry_date_entree = Gtk.Entry()
        entry_date_entree.set_placeholder_text("jj/mm/aaaa")
        grid.attach(entry_date_entree, 1, 4, 1, 1)

        # Champ de saisie pour la date de sortie
        label_date_sortie = Gtk.Label(label="Date de sortie")
        grid.attach(label_date_sortie, 0, 5, 1, 1)
        entry_date_sortie = Gtk.Entry()
        entry_date_sortie.set_placeholder_text("jj/mm/aaaa")
        grid.attach(entry_date_sortie, 1, 5, 1, 1)

        # Bouton pour valider la réservation
        button = Gtk.Button.new_with_label("Valider la réservation")
        button.connect("clicked", self.on_button_clicked)
        grid.attach(button, 0, 6, 2, 1)

        # Centrer les éléments dans la fenêtre
        grid.set_halign(Gtk.Align.CENTER)
        grid.set_valign(Gtk.Align.CENTER)

    def on_button_clicked(self, button):
    # Retrieve the values of the form fields
        nom = self.entry_nom.get_text()
        prenom = self.entry_prenom.get_text()
        telephone = self.entry_telephone.get_text()
        chambre = self.entry_chambre.get_text()
        date_entree = self.entry_date_entree.get_text()
        date_sortie = self.entry_date_sortie.get_text()

    # Create the request payload
        data = {
            'nom': nom,
            'prenom': prenom,
            'telephone': telephone,
            'chambre': chambre,
            'date_entree': date_entree,
            'date_sortie': date_sortie
    }

    # Send the HTTP request
        response = requests.post('http://your-api-endpoint.com/reservations', json=data)

        # TODO: handle the response status code and any errors that may occur


win = ReservationForm()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
