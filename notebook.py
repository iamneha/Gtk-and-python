#!/usr/bin/python
from gi.repository import Gtk
class MyWindow(Gtk.Window):
       def __init__(self):
	Gtk.Window.__init__(self, title="notebook")
	self.set_border_width(10)

	self.notebook = Gtk.Notebook()
	self.add(self.notebook)

	self.page1 = Gtk.Box()
	self.page1.set_border_width(10)
	self.page1.add(Gtk.Label('This is a notebook'))
	self.notebook.append_page(self.page1, Gtk.Label('First Note'))

	self.page2 = Gtk.Box()
	self.page2.set_border_width(10)
	self.page2.add(Gtk.Label('A page with an image title'))
	self.notebook.append_page(self.page2, Gtk.Image.new_from_icon_name("help-about", Gtk.IconSize.MENU))

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
