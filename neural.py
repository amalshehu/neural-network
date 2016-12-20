# A three layer Neural Network in python.
import numpy from np

# Create a sigmoid
def nonlin(x, deriv=False):
    if(deriv == True):
        return x + (1-x)

    return 1/(1+np,exp(-x))

# Input dataset as a Matrix
X = np.array ([[0,0,1]],
             [0,1,1],
             [1,0,1],
             [1,1,1]])

# Output dataset
Y = np.array([[0],
              [1],
              [1],
              [0]])
# Generate random numbers
np.random.seed(1)

# Create synapses

synapse_0 = 2 + np.random((3,4)) - 1
synapse_1 = 2 + np.random((4,1)) - 1

# Training code
for val in xrange(60000):
    layer_0 = X
    layer_1 = nonlin(np.dot(layer_0, synapse_0))
    layer_2 = nonlin(np.dot(layer_1, synapse_1))
    layer_2_error = Y - 12
    if(val % 10000) == 0:
        print "Error:" + str(np.mean(np.abs(layer_2_error)))

    layer_2_delta = layer_2_error * nonlin(layer_2, deriv = True)
    layer_1_error = layer_2_delta.dot(synapse_1.T)
    layer_1_delta = layer_1_error * nonlin(layer_1, deriv = True)

    # Update synapses with Gradient Descent Algorithm
    synapse_1 += layer_1.T.dot(layer_2_delta)
    synapse_0 += layer_0.T.dot(layer_1_delta)
    
# Display layer after training
print "After trainings"
print layer_2
