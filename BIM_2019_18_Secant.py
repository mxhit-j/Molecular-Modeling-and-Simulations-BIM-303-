# code to find root of an  
# equations using secant method  
  
# function takes value of x  
# and returns f(x)  
def f(x): 
      
  
    f = x**2 - 4*x - 10;  
    return f;  
  
def secant(x1, x2, E): 
    n = 0; xm = 0; x0 = 0; c = 0;
    while True:  
              
            # calculating the intermediate value  
        x0 = ((x1 * f(x2) - x2 * f(x1)) /
              (f(x2) - f(x1)));  
  
            # check if x0 is root of  equation or not  
        c = f(x1) * f(x0);  
  
            # updating the value of interval  
        x1 = x2;  
        x2 = x0;  
  
            # updating number of iteration  
        n += 1;  
  
            # if x0 is the root of equation, then break the loop  
        if (c == 0):  
            break;  
        xm = ((x1 * f(x2) - x2 * f(x1)) / 
                        (f(x2) - f(x1))); 
              
        if(abs(xm - x0) < E):  #termination criteria is set to f(x3) or the difference to be less
                                            #than E = 0.0001
            break; 
          
    print("Root of the given equation =",  
                               round(x0, 6));  
    print("No. of iterations = ", n);  
  
x1 = float(input('Enter the first value = '))
x2 = float(input('Enter the second value= '))
E = 0.0001
print('Minimum error = ', E)

if (f(x1) * f(x2) > 0):
    print("Can not find a root in the given inteval")
else:
    secant(x1, x2, E)
