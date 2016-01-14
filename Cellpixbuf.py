from gi.repository import Gtk
class CellRendererPixbuf(Gtk.Window):
       def __init__(self):
	Gtk.Window.__init__(self, title="Icons view")	
	self.set_default_size(200,200)

	self.liststore = Gtk.ListStore(str, str)

	self.liststore.append(["New", "document-new"])
	self.liststore.append(["open", "document-open"])
	self.liststore.append(["save", "document-save"])

	treeview = Gtk.TreeView(model = self.liststore)

	renderer_text = Gtk.CellRendererText()
	column_text = Gtk.TreeViewColumn("Text",renderer_text, text=0)
	treeview.append_column(column_text)

	renderer_pixbuf = Gtk.CellRendererPixbuf()

	column_pixbuf = Gtk.TreeViewColumn("Image", renderer_pixbuf, icon_name=1)
	treeview.append_column(column_pixbuf)
	self.add(treeview)

win = CellRendererPixbuf()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
