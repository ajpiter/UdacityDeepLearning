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
