#!/usr/bin/env python

from src.newrelic_indicator import *
from src.newrelic_app import *
from src.config_parser import *

if __name__ == "__main__":
    config = ConfigParser()
    config.read('config.json')

    app = NewrelicApp(config.get_value("API Key"), config.get_value("App ID"))

    indicator = NewrelicIndicator()
    indicator.set_app(app)
    indicator.run()
