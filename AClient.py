import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
class AddClientWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Ajouter un client")

        # Créer une grille pour organiser les éléments du formulaire
        grid = Gtk.Grid()
        self.add(grid)

        # Nom du client
        label_nom = Gtk.Label("Nom:")
        self.entry_nom = Gtk.Entry()
        grid.attach(label_nom, 0, 0, 1, 1)
        grid.attach(self.entry_nom, 1, 0, 1, 1)

        # Prénom du client
        label_Prenom = Gtk.Label("Prénom:")
        self.entry_Prenom = Gtk.Entry()
        grid.attach(label_Prenom, 0, 1, 1, 1)
        grid.attach(self.entry_Prenom, 1, 1, 1, 1)

      

        # Téléphone du client
        label_Telephone = Gtk.Label("Téléphone:")
        self.entry_Telephone = Gtk.Entry()
        grid.attach(label_Telephone, 0, 3, 1, 1)
        grid.attach(self.entry_Telephone, 1, 3, 1, 1)

 
        # Bouton Ajouter
        button_add = Gtk.Button(label="Ajouter")
        button_add.connect("clicked", self.on_button_add_clicked)
        grid.attach(button_add, 1, 5, 1, 1)
        # Centrer les éléments dans la fenêtre
        grid.set_halign(Gtk.Align.CENTER)
        grid.set_valign(Gtk.Align.CENTER)

    def on_button_add_clicked(self, button):
        Nom = self.entry_Nom.get_text()
        Prenom = self.entry_Prenom.get_text()
        Telephone = self.entry_Telephone.get_text()
      

   

win = AddClientWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
