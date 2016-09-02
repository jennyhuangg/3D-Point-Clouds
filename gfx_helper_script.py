# gfx_helper_script.py --- setup script for non-interactive plotting with
# Matplotlib in scripts.
#   By Jadrian Miles, December 2015
# 
# To use, just stick the following line at the top of your script:
# 
# from gfx_helper_repl import *
# 
# This will execute all the following commands in your script's global
# namespace.

import numpy as np
import matplotlib
# Set the Matplotlib backend to Tk, to prevent hangs.
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
# Turn off interactive mode, just in case.
plt.ioff()
# Load up 3D plotting tools too.
from mpl_toolkits.mplot3d import Axes3D
