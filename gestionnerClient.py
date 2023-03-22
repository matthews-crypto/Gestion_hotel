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

        ListClient_button = Gtk.Button(label="Liste des clients")
        ListClient_button.set_size_request(100, 100)
        grid.attach(ListClient_button, 0, 0, 1, 1)

        SuppClient_button = Gtk.Button(label="Suppression Client")
        grid.attach(SuppClient_button, 1, 0, 1, 1)

        AjoutClient_button = Gtk.Button(label="Ajouter Client")
        grid.attach(AjoutClient_button, 0, 1, 1, 1)

        Retour_button = Gtk.Button(label="Retour")
        grid.attach(Retour_button, 2, 0, 1, 1)

        grid.set_size_request(300, 100)

        ListClient_button.connect("clicked", self.ouvrir_gestion_ListClient)
        SuppClient_button.connect("clicked", self.ouvrir_gestion_SuppClient)

    def ouvrir_gestion_ListClient(self, widget):
        os.system('python Lis.py')

    def ouvrir_gestion_SuppClient(self, widget):
        os.system('python suppp.py')
window = MenuWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
