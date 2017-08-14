#Notes from Implementing Gradient Descent in Udacity's Deep Learning Degree 

#Example network has 3 input layers, 1 output layer
#using the Sigmoid Function for the output unit activation 

#One of the inputs has categorical numbers (1st place, 2nd place, 3rd place) without relative values. 
#2nd place is not twice as much as 1st place
#Split the data into the number of columns equal to the number of categories. 
#Then asign a 0 or 1 (for True or False) to each of the columns 
#Example 1stPlace would be the name of column 1, and for the first place winner would hold the value 1 

#Standardize the data 
#Scaling the data so they have a zero mean and standard deviation of 1 
#The sigmoid function squashes really small and really large inputs.
#The gradient of small/large numbers is 0 
#Making the gradient descent go to 0 too 
#With really large input numbers the gradient descent steps will die off and the network won't train.
#If we standarize the data we can initialize the weights 

