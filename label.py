#!/usr/bin/python
from gi.repository import Gtk
class LabelWindow(Gtk.Window):
       def __init__(self):
	Gtk.Window.__init__(self, title="Label")

	hbox = Gtk.Box(spacing = 10)
	hbox.set_homogeneous(False)
	vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
	vbox_left.set_homogeneous(False)
	vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
	vbox_right.set_homogeneous(False)

	hbox.pack_start(vbox_left, True, True, 0)
	hbox.pack_start(vbox_right, True, True, 0)

	label = Gtk.Label("This is a normal label")
	vbox_left.pack_start(label, True, True, 0)

	label = Gtk.Label()
	label.set_text("This is left-justified label\n with multile line")
	label.set_justify(Gtk.Justification.LEFT)
	vbox_left.pack_start(label, True, True, 0)

	label = Gtk.Label("This is just opposite to normal label")
	label.set_line_wrap(True)
	vbox_right.pack_start(label, True, True, 0)	

	label = Gtk.Label("This is right justified label")
	label.set_line_wrap(True)
	label.set_justify(Gtk.Justification.FILL)
	vbox_right.pack_start(label,True,True, 0)

	label = Gtk.Label()
	label.set_markup("This is an example to set label view according to you. Text cam be <small> small </small>, <big> big</big>, <b>bold</b> etc. ")
	label.set_line_wrap(True)
	vbox_left.pack_start(label, True, True, 0)

	button= Gtk.Button(label = "click ")
	label.set_mnemonic_widget(button)
	vbox_right.pack_start(button, True, True, 0)

	self.add(hbox)


window = LabelWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
