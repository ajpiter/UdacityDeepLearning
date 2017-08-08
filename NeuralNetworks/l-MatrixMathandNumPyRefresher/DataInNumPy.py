#ndarray objects 
#ndarray objects are similar to python lists but can have multiple dimensions
#ndarrays can represent scalars, vectors, matrices or tensors. 
#You can preform math bewteen ndarrays, NumPy scalars, and Python scalars. 

#NumPy Scalars 
#Are inside arrays 
#Can be signed or unsigned and can be different sizes
#Every vector, matrices, or tensor you make must be stored in a scalar. 
#You can specify the type but every item in the array must have the same time. 

#To create a NumPy array that holds a scalar
scalarvariable = np.array(5)
#To see the shape of the array 
scalarvariable.shape 
#empty parenthesis () after calling variable.shape indicates it has zero dimensions. 

#Vectors 
vectorvariable = np.array([1, 2, 3,]) 
vectorvariable.shape
#would return (3,) the one dimensional length of the list 
#xvariable = vectorvariable[indexnumber] or 
xvariable = vectorvariable[1]
#you can also use MunPy slicing in a vector 

#Matrices 
#Lists of Lists, where each list represents a row 
matrixvariable = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrixvariable.shape
#returns (3, 3) indicating two dimensions each with a length of 3
#you can use indexing to access elements of the matrix by 
matrixvariable[1][2]
#returns 6 

#Tensors 
#Tensors have more dimensions, below is an example of a 3x3x2x1 tensor
tensorvariable = np.array([[[[1],[2]],[[3],[4]],[[5],[6]]],[[[7],[8]],[[9],[10]],[[11],[12]]],[[[13],[14]],[[15],[16]],[[17],[17]]]])
tensorvariable.shape
#would return (3, 3, 2, 1) 
#index tensorvariable[2][1][1][0] would return 16 

#Changing Shapes 
#To change from vectors to a matrix 
vectorvariable = np.array([1,2,3,4]) 
vectorvariable.shape
#returns (4,) confirming the shape of a vector 
variable = vectorvariable.reshape(1,4) 
variable.shape
#returns (1, 4) confirming a row matrix 
#OR
variable = vectorvariable.reshape(4,1) 
#returns (4, 1) confirming a column matrix
#You can also drop the .reshape command all together and write 
variable = vectorvariable[None, :]
#OR 
variable = vectorvariable[:, None] 


