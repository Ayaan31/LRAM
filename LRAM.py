import math
import sympy as sym

#height = sym.Symbol('x')

#func =  (sym.sec(height)**2)  - height
global LRAM
LRAM = 0

global height
height = 0

print("Number of Subintervals: ", end = "")
num_subintervals = int(input())

print("Interval of Function in form (a, b)")

interval_a = int(input("a: "))
interval_b = int(input("b: "))

width = (interval_b - interval_a) / num_subintervals


for n in range(num_subintervals):
    if interval_a == 0 and n == 0:
        height += 0
        LRAM += (sym.sec(height)**2) - height
    else:
        height += interval_a + width
        LRAM += (sym.sec(height)**2) - height

LRAM = LRAM * width

print(round(LRAM, 3))
        
    
        
    


