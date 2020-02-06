# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Randall Woodall, Andres Acosta, Sarbajit Basu
# February 2020
# main.py
# Control center for the power flow program as described by Dr. Ranade.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from admittance import Admittance

test1 = Admittance(['line_1 bus_1 bus_2 5 17', 'line_2 bus_2 bus_3 4 10'])
print(test1.admittance)
test2 = Admittance(['line_1 1 2 5 17', 'line_2 2 3 4 10'])
