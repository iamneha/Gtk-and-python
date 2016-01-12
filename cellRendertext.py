from gi.repository import Gtk
class CellRenderText(Gtk.Window)
       def __init__(self):
	Gtk.Window.__init__(self, title="Text")
	self.set_default_size(200, 200)	

	self.liststore = Gtk.ListStore(str, str)
	self.liststore.append(["Fedora","http://fedoraproject.org/" ])
	self.liststore.append(["Fedora","http://fedoraproject.org/" ])

	treeview = Gtk.TreeView(model=self.liststore)

	renderer_text = Gtk.CellRendererText()
	column_text = Gtk.TreeViewColumn("Text,")
