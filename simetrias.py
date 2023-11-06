# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from matplotlib import pyplot as plt

f1 ='8-x'  #<=
f2='18-3x' #<=
x = symbols('x')

#graficar f1 y f2 solo en el primer cuadrante
sym.plotting.plot(f1, f2, xlim=[0,10], ylim=[0,10], title='Primer cuadrante', legend=True, show=False)