#Show the entry of any text, maximum length and to make it visible or not
#Text can be editable

from gi.repository import Gtk
class Entry(Gtk.Window):
       def __init__(self):
	Gtk.Window.__init__(self, title= "Entry window")
	self.set_size_request(200, 100)

	self.timedout_id= None
	
	vbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing=6)
	self.add(vbox)

	self.entry = Gtk.Entry()
	self.entry.set_text("Entry label")
	self.entry.set_max_length(20)
	vbox.pack_start(self.entry, True, True, 0)

	hbox = Gtk.Box(spacing = 6)
	vbox.pack_start(hbox, True, True, 0)

	self.check_editable = Gtk.CheckButton("Editable")
	self.check_editable.connect("toggled", self.on_editable_toggled)
	self.check_editable.set_active(True)
	hbox.pack_start(self.check_editable, True, True, 0)

	self.check_visible = Gtk.CheckButton("visible")
	self.check_visible.connect("toggled", self.on_visible_toggled)
	self.check_visible.set_active(True)
	hbox.pack_start(self.check_visible, True, True, 0)

	
       def on_editable_toggled(self, button):
	value = button.get_active()
	self.entry.set_editable(value)

       def on_visible_toggled(self, button):
	value = button.get_active()
	self.entry.set_visibility(value)

       

win = Entry()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
