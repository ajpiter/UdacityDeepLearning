#The shapes data can have 

A scalar is a single number.  

Vectors are lists of numbers with 1 dimension.
There can be row vectors or column vectors. 
Both row vectos and column vectors can store the same things, but which one you choose may affect the math you are able to do. 
Example of a row vector [1 2 3]. 
The dimension of a vector is the length of the vector.
Vectos can also be classified as a matrix.
The above row vector would be a 1 x 3 matrix. 
A column vector with the same numbers would be a 3 x 1 matrix.

Matrix are two dimensional grid of values. 
We describe the shape of a matrix in terms of the number of rows and columns. 
[ 1 2 3
  4 5 6 ] 
The above example is a 2 x 3 matrix 

We use an index to find the values in a matrix. 
In math books indexing from 1, in python indexing from 0. 
A = [ 1 2 3 
      4 5 6] 
The location of an index for the above matrix is written as Axy.
So A12 would return the value 6 in python or the value 2 in math textbooks. 

Tensors can refer to data with any n dimensional values. 
A scalr is a 0 dimensional tensor 
A vector is a 1 dimensional tensor
A matrix is a 2 dimensional tensor
Anything higher than 2 dimensional we just call a tensor 

