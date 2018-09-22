print("Tes")


import random
import math
x1 = 2
x2 = 3
def fungsi(x1,x2):
    return -1*math.fabs(math.sin(x1)*math.cos(x2)*math.exp(math.fabs(1-math.sqrt(x1*x1+x2*2)/math.pi)))

fungsi(x1,x2)
