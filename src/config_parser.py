import json
import os

class ConfigParser:

    def __init__(self):
        self.path = os.path.dirname(os.path.realpath(__file__))

    def read(self, filename):
        self.raw_config = json.load(open(self.path+'/../'+filename))

        return self.raw_config
