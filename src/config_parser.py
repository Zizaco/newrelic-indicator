import json
import os

class ConfigParser:

    raw_config = {}

    def __init__(self):
        self.path = os.path.dirname(os.path.realpath(__file__))

    def read(self, filename):
        self.raw_config = json.load(open(self.path+'/../'+filename))

        return self.raw_config

    def get_value(self, key):
        return self.raw_config[key] if (key in self.raw_config) else False
