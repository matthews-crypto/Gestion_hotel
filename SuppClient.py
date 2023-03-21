import requests
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ClientSupprimer(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Supprimer un client")
        
        # Créer une grille pour organiser les éléments du formulaire
        grid = Gtk.Grid()
        self.add(grid)

        # Téléphone du client
        label_tel = Gtk.Label("Téléphone:")
        self.entry_tel = Gtk.Entry()
        grid.attach(label_tel, 0, 0, 1, 1)
        grid.attach(self.entry_tel, 1, 0, 1, 1)

        # Ajouter un bouton pour supprimer le client
        supprimer_button = Gtk.Button(label="Supprimer")
        supprimer_button.connect("clicked", self.supprimer_client)
        grid.attach(supprimer_button, 0, 1, 2, 1)
        
        # Centrer les éléments dans la fenêtre
        grid.set_halign(Gtk.Align.CENTER)
        grid.set_valign(Gtk.Align.CENTER)

    def supprimer_client(self, widget):
        # Récupérer le numéro de téléphone saisi
        phone = self.entry_tel.get_text()

        # Envoyer une requête DELETE à l'API pour supprimer le client
        response = requests.delete(f"https://mon-api.com/clients/")

        # Vérifier si la suppression a réussi
        if response.status_code == 204:
            # Afficher un message de confirmation
            message = Gtk.MessageDialog(parent=self, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="Client supprimé")
            message.run()
            message.destroy()
        else:
            # Afficher un message d'erreur
            message = Gtk.MessageDialog(parent=self, flags=0, message_type=Gtk.MessageType.ERROR, buttons=Gtk.ButtonsType.OK, text="Erreur lors de la suppression du client")
            message.run()
            message.destroy()

win = ClientSupprimer()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
