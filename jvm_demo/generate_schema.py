#!/usr/bin/python 

import os
import sys

from pyfiglet import Figlet
figlet = Figlet(font='slant')


print("\n".join(f"# {i}" for i in figlet.renderText('OMG YAML!').splitlines()))
os.system(f"{sys.executable} print_schema.py")