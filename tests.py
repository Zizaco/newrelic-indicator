#!/usr/bin/env python

import os
import glob
import unittest

from src.newrelic_indicator import *
from src.newrelic_app import *
from src.config_parser import *

test_files = glob.glob("tests/"+os.path.dirname(__file__)+"/*.py")

for files in test_files:
    execfile(files)

if __name__ == '__main__':
    unittest.main()

