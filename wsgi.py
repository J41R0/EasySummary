#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import sys
import xintesis
from xintesis.engine import XthEngine

if __name__ == "__main__":
    xintesis.PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(os.path.abspath(os.path.dirname(__file__)))
    xintesis.core.init_core()
    XthEngine.run()

