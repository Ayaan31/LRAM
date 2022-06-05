import math
import sympy as sym

# Creates a global vairable which whill store the LRAM value
global LRAM
LRAM = 0

global height
height = 0

# Asks the user for the # of subintervals they want to use
print("Number of Subintervals: ", end = "")
num_subintervals = int(input())

# Asks the user for their upper and lower bounds
print("Interval of Function in form (a, b)")

interval_a = int(input("a: "))
interval_b = int(input("b: "))

# Calculates the width of each rectangle using the formula:   (b - a) / n
width = (interval_b - interval_a) / num_subintervals


# This for loop will run for the number given in the sub intervals
# For instance, if the # of subintervals is 4 then it runs 4 times
for n in range(num_subintervals):
    
    # For the first run, if the lower bound is 0 and no previous calculations have been done, plug in zero for the height
    if interval_a == 0 and n == 0:
        height += 0
        LRAM += (sym.sec(height)**2) - height
        
    # Otherwise calculate the height and plug that into the function: (sec(x)^2) - x
    # The values calculated on each run will be added to the LRAM variable 
    else:
        height += interval_a + width
        LRAM += (sym.sec(height)**2) - height

# Lastly multiply the LRAM variable by the width to get the actual LRAM
LRAM = LRAM * width

# Print the LRAM rounded to 3 decimal places
print(round(LRAM, 3))
        
