from mock import Mock

class NewrelicIndicatorTest(unittest.TestCase):

    def setUp(self):
        # Set
        self.original_setup          = NewrelicIndicator.setup
        self.original_build_menu     = NewrelicIndicator.build_menu

        # Mocks
        NewrelicIndicator.setup      = Mock()
        NewrelicIndicator.build_menu = Mock()

    def tearDown(self):
        # Restore original class methods
        if hasattr(self, 'original_setup'):
            NewrelicIndicator.setup      = self.original_setup

        if hasattr(self, 'original_build_menu'):
            NewrelicIndicator.build_menu = self.original_build_menu

    def test_should_instantiate(self):
        # Assertion
        ind = NewrelicIndicator()

        self.assertIsInstance(ind, NewrelicIndicator)
        assert NewrelicIndicator.setup.called
        assert NewrelicIndicator.build_menu.called

    def test_should_setup(self):
        # Set
        ind = NewrelicIndicator()
        NewrelicIndicator.setup      = self.original_setup

        # Mocks
        indicator_obj = Mock(name='Indicator')
        indicator_obj.set_status   = Mock()
        indicator_obj.set_label    = Mock()

        appindicator.Indicator     = Mock(return_value=indicator_obj)
        appindicator.STATUS_ACTIVE = Mock()

        # Assertion
        ind.setup()
        self.assertIn('src', ind.path)
        self.assertEquals(ind.indicator, indicator_obj)
        appindicator.Indicator.assert_called_once_with("newrelic-indicator", ind.path + "/icon.png", appindicator.CATEGORY_APPLICATION_STATUS)
        indicator_obj.set_status.assert_called_once_with(appindicator.STATUS_ACTIVE)
        indicator_obj.set_label.assert_called_once_with("New Relic")

    def test_should_build_menu(self):
        #Set
        ind = NewrelicIndicator()
        NewrelicIndicator.build_menu = self.original_build_menu

        # Mocks
        ind._NewrelicIndicator__add_menu_iten = Mock()

        # Assertion
        ind.build_menu()

        ind._NewrelicIndicator__add_menu_iten.assert_called_once_with('Quit', ind.quit)

    def test_should_add_menu_iten(self):
        # Set
        ind = NewrelicIndicator()

        # Mocks
        method_callback        = Mock(name='Method')
        menu_obj               = Mock(name='Menu')
        menu_obj.append        = Mock()
        menu_iten_obj          = Mock(name='MenuItem')
        menu_iten_obj.connect  = Mock()
        menu_iten_obj.show     = Mock()
        ind.indicator          = Mock(name='Indicator')
        ind.indicator.set_menu = Mock()

        gtk.Menu     = Mock(return_value=menu_obj)
        gtk.MenuItem = Mock(return_value=menu_iten_obj)

        # Assertion
        ind._NewrelicIndicator__add_menu_iten('ItemName', method_callback)

        gtk.MenuItem.assert_called_once_with('ItemName')

        self.assertEquals(ind.menu, menu_obj)
        menu_iten_obj.connect.assert_called_once_with("activate", method_callback)
        menu_iten_obj.show.assert_called_once()
        menu_obj.append.assert_called_once_with(menu_iten_obj)
        ind.indicator.set_menu.assert_called_once_with(menu_obj)

