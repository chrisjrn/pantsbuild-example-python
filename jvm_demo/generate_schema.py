#!/usr/bin/python

import os
import sys

from pyfiglet import Figlet

figlet = Figlet(font="slant")
    
print("\n".join(f"{i}" for i in figlet.renderText("dependencies!").splitlines()))
os.system(f"{sys.executable} print_schema.py" + f"> {sys.argv[1]}" if sys.argv[1] else "")
