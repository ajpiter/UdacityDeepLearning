#Gradient Descent 

#Take tiny steps towards a solution 

#We want to change the weights in steps that reduce the error
#By taking small steps in the direction that reduces the error the most
#We find this by calculating the gradient of the squared error 

#Error for one prediction
TrueTargetValue = y
NetworkOutput = y^
Error = (TrueTargetValue - NetworkOutput)Squared 
Error = (y - y^)^2

#Total Error for the network over the entire dataset 
SumMu = Sum Of the Error for each dataset 
SSE = SumoftheSquaredErrors 
SSE = (1/2)*(SumMu)(y - y^)^2 

#***Example of Gradient Descent with a Sigmoid function for activation***

# Defining the sigmoid function for activations
def sigmoid(x):
    return 1/(1+np.exp(-x))
# Derivative of the sigmoid function
def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Input data
x = np.array([0.1, 0.3])
# Target
y = 0.2
# Input to output weights
weights = np.array([-0.8, 0.5])
# The learning rate, eta in the weight step equation
learnrate = 0.5

# the linear combination performed by the node (h in f(h) and f'(h))
h = x[0]*weights[0] + x[1]*weights[1]
# or h = np.dot(x, weights)
# The neural network output (y-hat)
nn_output = sigmoid(h)
# output error (y - y-hat)
error = y - nn_output
# output gradient (f'(h))
output_grad = sigmoid_prime(h)
# error term (lowercase delta)
error_term = error * output_grad
# Gradient descent step 
del_w = [ learnrate * error_term * x[0],
          learnrate * error_term * x[1]]
# or del_w = learnrate * error_term * x
