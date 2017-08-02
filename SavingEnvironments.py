#In the terminal 
#Save the packages in your environments to a YAML file 
conda env export > filename.yaml

#To create an environment from a yaml file 
conda env create -f filename.yaml 
#The environment will have the same name as the yaml file 

#Listing environments 
#To see all the environments you've created on the computer
conda env list 
#The environment you are currently in appears with an * 
#The default environment is root 

#Removing environments 
conda env remove -n env_name
