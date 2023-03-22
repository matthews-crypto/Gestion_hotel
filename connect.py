import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class InscriptionForm(Gtk.Window):

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
        entry_telephone.set_placeholder_text("Numéro téléphone")
        grid.attach(entry_telephone, 1, 2, 1, 1)

        label_email = Gtk.Label(label="E-mail")
        grid.attach(label_email, 0, 3, 1, 1)

        self.entry_email = Gtk.Entry()
        grid.attach(self.entry_email, 1, 3, 1, 1)

        label_motdepasse = Gtk.Label(label="Mot de passe")
        grid.attach(label_motdepasse, 0, 4, 1, 1)

        self.entry_motdepasse = Gtk.Entry()
        self.entry_motdepasse.set_visibility(False)
        grid.attach(self.entry_motdepasse, 1, 4, 1, 1)

        label_confirmation = Gtk.Label(label="Confirmation  mot de passe")
        grid.attach(label_confirmation, 0, 5, 1, 1)

        self.entry_confirmation = Gtk.Entry()
        self.entry_confirmation.set_visibility(False)
        grid.attach(self.entry_confirmation, 1, 5, 1, 1)

        button = Gtk.Button(label="S'inscrire")
        button.connect("clicked", self.on_button_clicked)
        grid.attach(button, 0, 6, 2, 1)

        # Centrer les éléments dans la fenêtre
        grid.set_halign(Gtk.Align.CENTER)
        grid.set_valign(Gtk.Align.CENTER)
    def on_button_clicked(self, widget):
        prenom = self.entry_prenom.get_text()
        nom = self.entry_nom.get_text()
        telephone = self.entry_telephone.get_text()
        email = self.entry_email.get_text()
        motdepasse = self.entry_motdepasse.get_text()
        confirmation = self.entry_confirmation.get_text()


win = InscriptionForm()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
