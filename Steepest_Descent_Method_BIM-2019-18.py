#Steepest descent method
x1 = int(input('Enter the initial guess: '))

def f(x):
    p = 1 - (2*x)
    return p

fx1 = f(x1)
x2 = x1 + 0.1*f(x1)


while(True):
    if x2-x1 < 0.0001 and x2-x1 > -0.0001:
        break
    else:
        x1 = x2
        x2 = x1 + 0.1*f(x1)
print('The root is', x2)
       

