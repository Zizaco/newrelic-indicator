import json
import httplib

class NewrelicApp:

    def __init__(self, api_key, api_id):
        self.api_key = api_key
        self.api_id  = api_id
        self.raw_app = {}
        self.reachable = False

    def update_state(self):
        headers = {"X-Api-Key":self.api_key}
        url     ='/v2/applications/'+self.api_id+'.json'
        conn    = httplib.HTTPConnection('api.newrelic.com')

        try:
            conn.connect()
            conn.request('GET', url, '', headers)
            response = conn.getresponse()
            if response.status == 200:
                self.raw_app = json.loads(response.read())
                self.reachable = True
                return True
        except:
            print "Unable to connect"

        self.reachable = False
        return False

    def is_online(self):
        return self.reachable

    def get_rpm(self):
        return self.raw_app['application']['application_summary']['throughput'] if self.is_online() else False

    def get_response_time(self):
        return self.raw_app['application']['application_summary']['response_time'] if self.is_online() else False

    def get_errors(self):
        return self.raw_app['application']['application_summary']['error_rate'] if self.is_online() else False

    def get_info(self):
        return ("{0:.0f}".format(self.get_response_time())+"ms | "+str(self.get_rpm())+" rpm | "+"{0:.0f}".format(self.get_errors()*100)+"% errors") if self.is_online() else "info unavailable"

