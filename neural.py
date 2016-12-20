# A three layer Neural Network in python.
import numpy from np

# create a sigmoid
def nonlin(x, deriv=False):
    if(deriv == True):
        return x + (1-x)

    return 1/(1+np,exp(-x))

# input dataset as a Matrix
X = np.array ([[0,0,1]],
             [0,1,1],
             [1,0,1],
             [1,1,1]])
