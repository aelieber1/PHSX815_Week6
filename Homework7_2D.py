"""
Purpose: Homework #7 PHSX 815
Attempt with 2 Dimensional Function
University of Kansas

author: @aelieber1  
other sources: 
    Monte Carlo Integration in Python examples: 
        - https://www.geeksforgeeks.org/monte-carlo-integration-in-python/
        - Monte Carlo Integration in Python tutorial: 
          https://www.youtube.com/watch?v=7RcqDi3txUE&t=0s (has another video for 2 
          dimensional MC integration

"""

# Import necessary functions
import scipy.integrate as spi
import numpy as np
import random
import sys
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # User inputted parameters    
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print (" -Nint: [integer # of sub intervals]")
        print (" -upperx: [upper x limit of integration]")
        print (" -lowerx: [lower x limit of integration]")
        print (" -uppery: [upper y limit of integration]")
        print (" -lowery: [lower y limit of integration]")
        sys.exit(1)

    # default lower bound for x
    a = 0
    
    # default upper bound for x
    b = 10
    
    # default lower bound for y
    c = 0
    
    # default upper bound for y 
    d = 10
    
    # default number of sub intervals
    Nint = 1000
   
    # read the user-provided input from the command line (if there)
    if '-Nint' in sys.argv:
        p = sys.argv.index('-Nint')
        Nint = int(sys.argv[p+1])
    if '-upperx' in sys.argv:
        p = sys.argv.index('-upperx')
        utemp = float(sys.argv[p+1])
        if utemp > 0:
            b = utemp
    if '-lowerx' in sys.argv:
        p = sys.argv.index('-lowerx')
        ltemp = int(sys.argv[p+1])
        if ltemp > 0:
            a = ltemp
    if '-uppery' in sys.argv:
        p = sys.argv.index('-uppery')
        utemp = float(sys.argv[p+1])
        if utemp > 0:
            d = utemp
    if '-lowery' in sys.argv:
        p = sys.argv.index('-lowery')
        ltemp = int(sys.argv[p+1])
        if ltemp > 0:
            c = ltemp
    
    # Define the function
    def f(x, y):
        return 5*x**3*y**2
    
    # plot of function for quick inspection
    x = np.linspace(a, b, 100)
    y = np.linspace(c, d, 100)
    plt.plot(f(x,y), color='red')
    plt.title("Plot of Function 5x^3y^2 from x=1 to x=10")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()
    
    # generate required random numbers between the limits
    x = []
    y = []
    for i in range(Nint):
        x.append(np.random.uniform(a,b))
        y.append(np.random.uniform(c,d))
        
    # compute summation
    summ = 0.0
    for r in range(Nint):
        summ += f(x[r],y[r])
        
    # compute the integration
    ans = (b-a)*(d-c)/float(Nint) * summ
    print("The integrated value using Monte Carlo Integration method is: ", ans)
    actual_integral = 4166666.6666666
    error = abs((actual_integral - ans)/actual_integral)
    print("The percent error versus the analytical integral is: ", error * 100, "%")
    
    print("As the number of sub intervals increases, the MC interval becomes more and more accurate (converging on truth), this can be tested by testing a variation of Nint values")