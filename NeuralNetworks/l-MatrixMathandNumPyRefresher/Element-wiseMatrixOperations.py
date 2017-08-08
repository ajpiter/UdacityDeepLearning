#Scalar Math 
#Is basic addition, multiplication etc but preformed on numerous numbers in a neural network. 
#In a program you might write a loop to do the same operation on every value in a list. 

#Matrices 
#If you have all the numbers stored in a matix you can perform element wise operations on them. 
#Element wise operations can apply to data with any number of dimensions. 

#Adding two scalars 
2 + 3 = 5 

#Adding a scalar and a matrix
#represented on paper by 
#2 + [ 1 2  = [3 4
#      3 4 ]   5 6] 

      
#Adding two matices 
#Have to be the same shape, cannot add a (2, 2) matrix with a (3, 4) matrix 
#represented on paper
#[ 1 3   +   [ 2 4   =   [ 3 7
# 5 7]        6 8]        11 15] 
a = np.array([[1, 3], [5,7]])
b = np.array([[2, 4], [6,8]]) 
a + b 
#returns array([[3, 7], 
#               [11, 15]])
