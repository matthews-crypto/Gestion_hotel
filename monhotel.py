import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os

class MenuWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Menu")
        self.set_border_width(10)

        box = Gtk.Box()
        box.set_halign(Gtk.Align.CENTER)
        box.set_valign(Gtk.Align.CENTER)
        self.add(box)

        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)
        box.pack_start(grid, True, True, 0)

        Hotel_button = Gtk.Button(label="Mon Hotel")
        Hotel_button.set_size_request(100, 100)
        grid.attach(Hotel_button, 0, 0, 1, 1)

        Chambres_button = Gtk.Button(label="Les chambres")
        grid.attach(Chambres_button, 1, 0, 1, 1)

        Clients_button = Gtk.Button(label="Les clients")
        grid.attach(Clients_button, 2, 0, 1, 1)

        Reservations_button = Gtk.Button(label=" reservations")
        Reservations_button.set_size_request(100, 100)
        grid.attach(Reservations_button, 0, 1, 1, 1)

        Factures_button = Gtk.Button(label="Gestion des factures")
        grid.attach(Factures_button, 1, 1, 1, 1)

        Statistiques_button = Gtk.Button(label="Statistiques")
        grid.attach(Statistiques_button, 2, 1, 1, 1)

        grid.set_size_request(300, 100)

        Hotel_button.connect("clicked", self.ouvrir_gestion_hotel)
        Chambres_button.connect("clicked", self.ouvrir_gestion_chambres)
        Clients_button.connect("clicked", self.ouvrir_gestion_client)


    def ouvrir_gestion_hotel(self, widget):
        os.system('python3 connect.py')
    def ouvrir_gestion_chambres(self, widget):
        os.system('pytho gestionChambre.py')
    def ouvrir_gestion_client(self, widget):
        os.system('pytho gestionClient.py')
    



window = MenuWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
