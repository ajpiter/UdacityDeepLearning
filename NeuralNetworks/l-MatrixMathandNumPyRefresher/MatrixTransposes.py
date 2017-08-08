#Matrix Transpose 
#A matrix with the same values as the orginal but it has the rows and columns switched 

#[ 1 2 3 4 
  5 6 7 8] 
#Transposes 
# [ 1 5 
#   2 6 
#   3 7 
#   4 8} 

#If the orgnial matrix is not a square the transpose has a new shape 
#Helpful if you need to perform a matrix multipication but your matrices are incompatible. 
#Make sure you are combing the right data 
#The only time you can safely use a transpose in a matrix multipication is if the data in both your orginal matrices is arranged as rows. 

#In MunPy to get a transponse just use T
m = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]]) 
m.T
#returns array([[1, 5, 9], 
#               [2, 6, 10], 
#               [3, 7, 11], 
#               [4, 8, 12]])


inputs = np.array([[-0.27, 0.45, 0.64, 0.31]])
inputs.shape
#returns (1, 4) 
weights = np.array([[0.02, 0.001, -0.03, 0.36], [0.04, -0.003, 0.025, 0.009], [ 0.012, -0.045, 0.28, -0.067]])
weights.shape
#returns (3, 4) 
np.matmul(inputs, weights) 
#returns a ValueError 
np.matmul(inputs, weights.T)
#returns array([[-0.01299, 0.00664, 0.13494]])
#OR 
np.matmul(weights, inputs.T) 
#returns array([[-0.01299], [0.00664], [0.13494]])

