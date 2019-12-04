#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/bokeh_v1/")

from bokeh_v1 import app as application
from bokeh_v1 import plot 
from bokeh_v1 import forms
from bokeh_v1 import assn2_module
from bokeh_v1 import assn3_module
from bokeh_v1 import proj_module
