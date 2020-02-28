# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Randall Woodall, Andres Acosta, Sarbajit Basu
# February 2020
# main.py
# Control center for the power flow program as described by Dr. Ranade.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from admittance import Admittance
from newtonRaphson import NewtonRaphson

import sys
import numpy as np

test1 = Admittance(open(sys.argv[1], 'r+').readlines())
powerFlow = NewtonRaphson(test1)

np.set_printoptions(linewidth=5000)
print(test1.admittance)

