#Store weights as a matrix indexed as w subscript ij 
#Each row corresponds to the weight leading out of a input node (or hidden node)
#Each column corresponds to the weight leading into a hidden node (or output) 

#To create a Matrix (also called a 2D array) called weightsinputtohidden

#Number of records and input units 
nrecords, ninputs = features.shape
#number of hidden units 
nhidden = 2 
weightsinputtohidden = np.random.normal(0, ninputs**-0.5, size=(ninputs, nhidden) 
#Matrix multiplication 
hiddeninputs = np.dpt(inputs, weightinputtohidden) 

#To get the transpose when you want a column vector and have a row vector
