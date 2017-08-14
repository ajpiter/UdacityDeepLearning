#Useful when using a lot of data, as opposed to the Sum Square Error (SSE) 

#Regardless of how much data we use our learning rate should be bewteen 0.01 and 0.001
#Using MSE to calculate the gradient 

#To update the weights with Gradient descent 
#Set the weight step to zero
#For each record in the training data 
#     Make a forward pass through the network calculating the output 
#     Calculate the error term for the output unit 
#     Update teh weight step 
#Update the weights; weights = weights + (learningrate *Weights.sum())/ numberofrecords 
#Repeat for e epochs 

#Implementing with NumPy 
#Initialize the weights 
weights = np.random.normal(scale=1/n_features**.5, size=n_features)
#NumPy calculates the dot product of two arrays calculating h for us 
#input to output layer 
output_in = np.dot(weights, inputs) 
#update the weights 
weights += weights ... 

