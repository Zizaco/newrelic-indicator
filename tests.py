#!/usr/bin/env python

import sys
import os
import glob
import unittest
from mock import Mock

# Mocks Module dependencies
sys.modules['gtk']          = Mock(name='gtk_module')
sys.modules['appindicator'] = Mock(name='appindicator_module')

# Import src modules
from src.newrelic_indicator import *
from src.newrelic_app import *
from src.config_parser import *

# Load test files
test_files = glob.glob("tests/"+os.path.dirname(__file__)+"/*.py")

for files in test_files:
    execfile(files)

# Run test
if __name__ == '__main__':
    unittest.main()

