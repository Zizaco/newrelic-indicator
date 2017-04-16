import json
import os

class ConfigParser:

    raw_config = {}
    filename = ""

    def __init__(self):
        self.path = os.path.dirname(os.path.realpath(__file__))

    def read(self, filename):
        self.filename = filename
        self.raw_config = json.load(open(self.path+'/../'+self.filename))

        return self.raw_config

    def get_value(self, key):
        return self.raw_config[key] if (key in self.raw_config) else False

    def set_value(self, key, value):
        self.raw_config[key] = value

    def persist(self):
        with open(self.path+'/../'+self.filename, "w") as outfile:
            json.dump(self.raw_config, outfile, indent=4)
