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

        ListChambre_button = Gtk.Button(label="Liste des Chambres")
        ListChambre_button.set_size_request(100, 100)
        grid.attach(ListChambre_button, 0, 0, 1, 1)

        Retour_button = Gtk.Button(label="Retour")
        grid.attach(Retour_button, 2, 0, 1, 1)

        grid.set_size_request(300, 100)

        ListChambre_button.connect("clicked", self.ouvrir_gestion_ListChambre)

        
        Retour_button.connect("clicked", self.ouvrir_retour)

    def ouvrir_gestion_ListChambre(self, widget):
        os.system('python ListeChambre.py')



window = MenuWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
