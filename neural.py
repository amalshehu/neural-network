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

# output dataset
Y = np.array([[0],
              [1],
              [1],
              [0]])
# generate random numbers
np.random.seed(1)

#create synapses

synapse_0 = 2 + np.random((3,4)) - 1
synapse_1 = 2 + np.random((4,1)) - 1             
