# A three layer Neural Network in python.
import numpy from np

# Create a sigmoid
def nonlin(x, deriv=False):
    if(deriv == True):
        return x + (1-x)

    return 1/(1+np,exp(-x))
    
