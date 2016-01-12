from gi.repository import Gtk
class CellRendererText(Gtk.Window):
       def __init__(self):
	Gtk.Window.__init__(self, title="Text")
	self.set_default_size(200, 200)	

	self.liststore = Gtk.ListStore(str, str)
	self.liststore.append(["Fedora","http://fedoraproject.org/" ])
	self.liststore.append(["Facebook","https://web.facebook.com/profile.php?id=100001996874688" ])
	self.liststore.append(["Github","https://github.com/iamneha"])

	treeview = Gtk.TreeView(model=self.liststore)

	renderer_text = Gtk.CellRendererText()
	column_text = Gtk.TreeViewColumn("Text", renderer_text, text=0)
	treeview.append_column(column_text)

	renderer_editabletext = Gtk.CellRendererText()
	renderer_editabletext.set_property("editable", True)

	column_editabletext = Gtk.TreeViewColumn("Editable text", renderer_editabletext, text=1)
	treeview.append_column(column_editabletext)
	
	renderer_editabletext.connect("edited", self.text_edited)

	self.add(treeview)

       def text_edited(self, widget, path, text):
	self.liststore[path][1] = text
win = CellRendererText()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
