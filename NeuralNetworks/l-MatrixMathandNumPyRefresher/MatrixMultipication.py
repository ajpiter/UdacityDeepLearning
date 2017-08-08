#Multipication a matrix 

#Element Wise Matrix multipication 
m = np.array([1,2,3], [4,5,6]])
n = m * .25 
#returns array([[0.25, 0.5, 0.77], 
#                [1. , 1.25, 1.5]])
m * n 
#returns array([[0.25, 1.0, 2.25],
#               [4.0, 6.25, 9.0]]) 
#OR 
np.multiply(m,n) 
#returns the same array 
#array([[0.25, 1.0, 2.25],
#       [4.0, 6.25, 9.0]]) 


#Matrix Product 
#Represented on Paper By 
#[ 1 2 3     [ 1 2 3     [30 36 42 
#  4 5 6  *    4 5 6  =   66 81 96 
#  7 8 9]      7 8 9]     102 126 150] 

#In a Matrix product you take the rows from the first matrix and the columns from the second 
#The number of columns in the left matrix must equal the number of rows in the right matrix 
#The answer matrix always has the same number of rows as the left matrix and the same number of columns as the right matrix. 
#Order matters 
#Data in the left matrix should be arranged as rows, while data in the right matrix should be arranged as columns 

a = np.array([[1,2,3,4], [5,6,7,8]])
a.shape 
#returns (2,4) 
b = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
b.shape
#returns (4,3) 
c = np.matmul(a, b) 
#returns array([[ 70, 80, 90],
#               [158, 184, 210]])
c.shape
#returns (2,3) 

#Dot Product 
#Two equal length vectors and convert those vectors into a single number 
# [0 2 4 6] [1 7 13 19] 
(0* 1) + (2 * 7) + (4 *13) + (6 *19) = 180 
#The results of a dot product and a matmul are the same if the matrices are two dimensional
a = np.array([[1,2],[3,4]])
np.dot(a,a) 
#OR 
a.dot(a)
#OR
np.matmul(a, a) 
#All return the same result 
#array([[7, 10], 
        [15, 22]])
