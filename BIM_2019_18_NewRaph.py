# Code for implementation of Newton 
# Raphson Method for solving equations 


# The function is:  
def func( x ): 
	return x**2 - 4*x - 10

# Derivative of the above function 
# which is 2*x - 4
def derivFunc( x ): 
	return 2*x - 4

# Function to find the root 
def newtonRaphson( x ):
	h = func(x) / derivFunc(x)
	#print('Iteration-%d, h=%0.6f and derivFunc(h) = %0.6f%'%(count,h,derivFunc(h)))
	while abs(h) >= 0.0001: 
		h = func(x)/derivFunc(x) 
		
		# x(i+1) = x(i) - f(x) / f'(x) 
		x = x - h 
	
	print("The value of the root is : ", 
		                     "%.4f"% x) 


x1 = float(input("Enter a guess value = "))
newtonRaphson(x1)
