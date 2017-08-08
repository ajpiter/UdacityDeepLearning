#Perceptrons 
#Also known as neurons 

#Inputs 

#Weights 
#Start out as random values, then as the neural network learns more about the input data and results the network adjusts the weights
#The process of adjusting the weights is called training the neural network 
#The higher the weight the more important it is in determining the output
# 'W' represents a matrix of weights 
# 'w' represents an indivdual weight

#Linear combination 
#Multiple weights times inputs and sum them 
  #Start at i = 1 
  #Evaluate (w1 * x1) and remember the results 
  #move to i = 2 
  #Evaluate (w2 * x2) and add these results to (w1 * x1) 
  #Continue repeating that process until i = mi where m is the number of inputs
#Example, if we had two inputs, (w1 * x1) + (w2 * x2) 

#Output signal 
#Done by feeding the linear combination into an activation function 
#Activation functions are functions that decide, given the inputs to the node what should be the nodes outputs. 
#The output layer is referred to as activations 

#Heaviside step function 
#An activation function that returns a 0 if the linear combination is less than 0. 
#It returns a 1 if the linear combination is positive or equal to zero. 
#Think of 1 as yes and 0 as no or True/False 

#Bias 
#one way to get a function to return 1 for more inputs is to add a value to the results of the linear combination 
#Bias is represented in equations as b 
#Similar to weights the bias can be updated and changed by the neural network durning training

#weights and bias are initially assigned a random value and then they are updated using a learning algorithm like gradient descent. 
#The weights and biases change so that the next training example is more accurate and patterns are learned by the neural network. 
