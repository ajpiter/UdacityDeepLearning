#The sigmoid Activation Function is also known as the logistic function 

#The sigmoid function is bounded bewteen 0 and 1 
#The output equals the probability for success 
#Same formula as logistic regression 

# Defining the sigmoid function for activations
def sigmoid(x):
    return 1/(1+np.exp(-x))

# Derivative of the sigmoid function
def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))

import numpy as np
def sigmoid(x): 
    return 1/(1 + np.exp(-x))
inputs = np.array([0.7, -0.3])
weights = np.array([0.1, 0.8])
bias = -0.1 
output = sigmoid(np.dot(weights, inputs) + bias) 
print(output) 

