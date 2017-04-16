import gtk
from src.config_parser import *

class ConfigWindow:

    current_tr = 0
    current_td = 0

    def __init__(self):
        self.setup()

    def setup(self):
        self.window = gtk.Window()
        self.window.set_title("NewRelic Indicator Configuration")
        self.window.set_border_width(15)

        self.box = gtk.Table(4, 3, True)
        self.window.add(self.box)

        self.prepare_window_elements()
        self.assemble_window_elements()

    def prepare_window_elements(self):
        self.label_api_key = gtk.Label('API Key')
        self.label_api_key_help = gtk.Label()
        self.label_api_key_help.set_markup('<i>NewRelic\'s API Key of your account</i>')
        self.text_api_key = gtk.Entry()
        self.label_api_id = gtk.Label('API ID')
        self.label_api_id_help = gtk.Label()
        self.label_api_id_help.set_markup('<i>The number in your app url at NewRelic</i>')
        self.text_api_id = gtk.Entry()
        self.btn_close = gtk.Button(stock=gtk.STOCK_CLOSE)
        self.btn_save = gtk.Button(stock=gtk.STOCK_APPLY)

    def assemble_window_elements(self):
        self.add_element(self.label_api_key)
        self.add_element(self.text_api_key, 2)
        self.line_break()
        self.skip()
        self.add_element(self.label_api_key_help, 2)
        self.line_break()
        self.add_element(self.label_api_id)
        self.add_element(self.text_api_id, 2)
        self.line_break()
        self.skip()
        self.add_element(self.label_api_id_help, 2)
        self.line_break()
        self.add_element(gtk.HSeparator(), 3)
        self.line_break()
        self.skip()
        self.add_element(self.btn_save)
        self.add_element(self.btn_close)

        self.registerEvents()

    def skip(self, size=1):
        self.current_td += size

    def line_break(self):
        self.current_td = 0
        self.current_tr += 1

    def add_element(self, element, size=1):
        self.box.attach(element, self.current_td, self.current_td+size, self.current_tr, self.current_tr+1)
        self.current_td += size
        element.show()

    def open(self):
        self.box.show()
        self.populate_fields()
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.show()
        self.window.set_keep_above(True)

    def registerEvents(self):
        self.btn_close.connect('clicked', self.close, None)
        self.window.connect("delete_event", self.close, None)

    def close(self, widget, data=None, foo=None):
        self.window.hide()
        return True

    def populate_fields(self):
        config = ConfigParser()
        config.read('config.json')
        self.text_api_key.set_text(config.get_value("API Key"))
        self.text_api_id.set_text(config.get_value("App ID"))

