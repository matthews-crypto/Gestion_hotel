import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import requests

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Liste de données")
        self.set_border_width(10)
        self.set_size_request(500, 500)

        self.list_store = Gtk.ListStore(str, str, str, str, str)

        data = requests.get("http://url_de_l_api/donnees").json()
        for d in data:
            self.list_store.append([d['Nom'], d['Prenom']d['Telephone']])

        self.treeview = Gtk.TreeView(model=self.list_store)

        for i, column_title in enumerate(["Nom", "Prenom","Téléphone"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)

        self.add(self.treeview)
        self.show_all()

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
