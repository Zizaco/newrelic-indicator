import json
import httplib

class NewrelicApp:

    def __init__(self, config_parser):
        self.config_parser = config_parser
        self.raw_app = {}
        self.reachable = False

    def update_state(self):
        headers = {"X-Api-Key":self.config_parser.get_value("API Key")}
        url     ='/v2/applications/'+self.config_parser.get_value("App ID")+'.json'
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
        if self.is_online():
            throughput = self.raw_app['application']['application_summary']['throughput']
        else:
            throughput = False

        if throughput > 1000:
            throughput = "{0:.1f}".format(throughput*0.001)+"k "

        return throughput

    def get_response_time(self):
        return self.raw_app['application']['application_summary']['response_time'] if self.is_online() else False

    def get_errors(self):
        return self.raw_app['application']['application_summary']['error_rate'] if self.is_online() else False

    def get_info(self):
        return ("{0:.0f}".format(self.get_response_time())+"ms | "+str(self.get_rpm())+"rpm | "+"{0:.1f}".format(self.get_errors()*100)+"% errors") if self.is_online() else "info unavailable"

