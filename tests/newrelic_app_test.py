from mock import Mock

class NewrelicAppTest(unittest.TestCase):

    def test_should_instantiate(self):
        # Set
        app = NewrelicApp('1111','777')

        # Assertion
        self.assertIsInstance(app, NewrelicApp)
        self.assertEquals(app.api_key,'1111')
        self.assertEquals(app.api_id,'777')
        self.assertFalse(app.reachable)

    def test_should_update_state_if_available(self):
        # Set
        app = NewrelicApp('1111','777')
        headers = {"X-Api-Key":'1111'}
        url     ='/v2/applications/777.json'

        # Mocks
        connection_obj         = Mock()
        response_obj           = Mock()
        httplib.HTTPConnection = Mock(return_value=connection_obj)

        response_obj.status        = 200
        response_obj.read          = Mock(return_value='{"some":"json"}')
        connection_obj.connect     = Mock()
        connection_obj.request     = Mock()
        connection_obj.getresponse = Mock(return_value=response_obj)

        # Assertion
        app.update_state()

        connection_obj.connect.assert_called_once()
        connection_obj.request.assert_called_once_with('GET', url, '', headers)
        connection_obj.getresponse.assert_called_once()

        self.assertEquals(app.raw_app, {"some":"json"})
        self.assertTrue(app.reachable)

    def test_should_not_update_state_if_unaavailable(self):
        # Set
        app = NewrelicApp('1111','777')
        headers = {"X-Api-Key":'1111'}
        url     ='/v2/applications/777.json'

        # Mocks
        connection_obj         = Mock()
        response_obj           = Mock()
        httplib.HTTPConnection = Mock(return_value=connection_obj)

        response_obj.status        = 500 # Error
        response_obj.read          = Mock(return_value='')
        connection_obj.connect     = Mock()
        connection_obj.request     = Mock()
        connection_obj.getresponse = Mock(return_value=response_obj)

        # Assertion
        app.update_state()

        connection_obj.connect.assert_called_once()
        connection_obj.request.assert_called_once_with('GET', url, '', headers)
        connection_obj.getresponse.assert_called_once()

        self.assertFalse(app.reachable)

    def test_should_check_is_online(self):
        # Set
        app = NewrelicApp('1111','777')

        # Assert
        app.reachable = True
        self.assertTrue(app.is_online())

        app.reachable = False
        self.assertFalse(app.is_online())

    def test_should_get_rpm(self):
        # Set
        app = NewrelicApp('1111','777')
        app.raw_app = {'application':{'application_summary':{'throughput':300}}}

        # Assert
        app.reachable = True
        self.assertEquals(300, app.get_rpm())

        app.reachable = False
        self.assertFalse(app.get_rpm())

    def test_should_get_rpm_greater_than_1k(self):
        # Set
        app = NewrelicApp('1111','777')
        app.raw_app = {'application':{'application_summary':{'throughput':3000}}}

        # Assert
        app.reachable = True
        self.assertEquals('3.0k ', app.get_rpm())

        app.reachable = False
        self.assertFalse(app.get_rpm())

    def test_should_get_response_time(self):
        # Set
        app = NewrelicApp('1111','777')
        app.raw_app = {'application':{'application_summary':{'response_time':100}}}

        # Assert
        app.reachable = True
        self.assertEquals(100, app.get_response_time())

        app.reachable = False
        self.assertFalse(app.get_response_time())

    def test_should_get_errors(self):
        # Set
        app = NewrelicApp('1111','777')
        app.raw_app = {'application':{'application_summary':{'error_rate':3}}}

        # Assert
        app.reachable = True
        self.assertEquals(3, app.get_errors())

        app.reachable = False
        self.assertFalse(app.get_errors())

    def test_should_get_info(self):
        # Set
        app = NewrelicApp('1111','777')

        # Mocks
        app.get_rpm           = Mock(return_value='300')
        app.get_response_time = Mock(return_value=85.9)
        app.get_errors        = Mock(return_value=0.50)

        # Asset
        app.reachable = True
        self.assertEquals('86ms | 300rpm | 50.0% errors', app.get_info())

        app.reachable = False
        self.assertEquals('info unavailable', app.get_info())
