# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Randall Woodall, Andres Acosta, Sarbajit Basu
# March 2020
# admittance.py
# Accept a list of lines and produce an admittance matrix.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class NewtonRaphson:
    # Accepts admittance which is an object of type Admittance
    def __init__(self, admittance):
        print('Newton Raphson Implementation')
        self.admittance = admittance
