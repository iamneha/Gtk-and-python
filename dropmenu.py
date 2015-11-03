#/usr/bin/python
from gi.repository import Gtk

class App(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title='ComboBox Test')

        model = Gtk.ListStore(int, str)
        for i in [[1, 'One'], [2, 'Two'], [3, 'Three'], [4, 'Four']]:
            model.append(i)

        combo = Gtk.ComboBox.new_with_model(model)
        renderer = Gtk.CellRendererText()

        combo.set_active(0)
        combo.pack_start(renderer, True)
        combo.add_attribute(renderer, 'text', 1)
        combo.connect('changed', self._changed_cb)

        self.add(combo)

        # Variables
        self.combo = combo
        self.model = model

    def _changed_cb(self, widget, param=None):
        comboiter = self.combo.get_active_iter()
        if comboiter:
            print("Changed to {}".format(
                     self.model.get_value(comboiter, 0)
            ))
        else:
            print("Nothing selected!")

win = App()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()
