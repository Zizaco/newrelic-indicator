import sys
import os
import gtk
import appindicator

class NewrelicIndicator:

    ping_frequency = 10 # seconds

    def __init__(self):
        self.setup()
        self.build_menu()

    def setup(self):
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.indicator = appindicator.Indicator("newrelic-indicator", self.path + "/icon.png", appindicator.CATEGORY_APPLICATION_STATUS)
        self.indicator.set_status(appindicator.STATUS_ACTIVE)
        self.indicator.set_label("New Relic")

    def build_menu(self):
        self.__add_menu_iten('Quit', self.quit)

    def __add_menu_iten(self, name, method):
        if not hasattr(self, 'menu'):
            self.menu = gtk.Menu()
            self.indicator.set_menu(self.menu)

        item = gtk.MenuItem(name)
        item.connect("activate", method)
        item.show()
        self.menu.append(item)

    def run(self):
        # self.check_newrelic()
        # gtk.timeout_add(ping_frequency * 1000, self.check_newrelic)
        gtk.main()

    def quit(self, widget):
        sys.exit(0)
