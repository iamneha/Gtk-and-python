#Button and there function
from gi.repository import Gtk
class Button(Gtk.Window):
       def __init__(self):
	Gtk.Window.__init__(self, title="Button")
	self.set_border_width(10)

	hbox = Gtk.Box(spacing = 6)
	self.add(hbox)
	
	button = Gtk.Button.new_with_label("click me")
	button.connect("clicked", self.on_click_me_clicked)
	hbox.pack_start(button, True, True, 0)
	
	button = Gtk.Button.new_with_mnemonic("_Open")
	button.connect("clicked", self.on_open_clicked)
	hbox.pack_start(button, True, False, 0)

	button = Gtk.Button.new_with_mnemonic("_close")
	button.connect("clicked", self.on_close_clicked)
	hbox.pack_start(button, True, True, 0)

	button = Gtk.ToggleButton("Toggle 1")
	button.connect("toggled", self.on_button_toggled, "Toggled 1")
	hbox.pack_start(button, True, True, 0)

	button = Gtk.ToggleButton("Toggle 2")
	button.set_active(True)
	button.connect("toggled", self.on_button_toggled, "Toggled 2")
	hbox.pack_start(button, True, True, 0)

	adjustment = Gtk.Adjustment(0, 0, 100, 1, 10, 0)
	self.spinbutton = Gtk.SpinButton()
	self.spinbutton.set_adjustment(adjustment)
	hbox.pack_start(self.spinbutton, False, False, 0)

	check_numeric = Gtk.CheckButton("Numeric")
	check_numeric.connect("toggled", self.on_numeric_toggled)
	hbox.pack_start(check_numeric, False, False, 0)

       def on_click_me_clicked(self, button):
	print("\"click me \" button was clicked")
       def on_open_clicked(self, button):
	print("\"open\" button was clicked")
       def on_close_clicked(self, button):
	print("closing application")
	Gtk.main_quit()
       def on_button_toggled(self, button, name):
	if button.get_active():
	   state = "on"
	else:
	   state = "off"
	print("Button", name, "was turned", state)
       def on_numeric_toggled(self, button):
	self.spinbutton.set_numeric(button.get_active())
win = Button()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
