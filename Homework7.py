"""
Purpose: Homework #7 PHSX 815
University of Kansas

author: @aelieber1  
other sources: 
    - https://www.geeksforgeeks.org/monte-carlo-integration-in-python/
    - Monte Carlo Integration in Python tutorial: 
      https://www.youtube.com/watch?v=7RcqDi3txUE&t=0s

"""

# Import necessary functions
import scipy.integrate as spi
import numpy as np
from scipy import random
import sys
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # User inputted parameters    
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print (" -Nint: [integer # of sub intervals]")
        print (" -upper: [upper limit of integration]")
        print (" -lower: [lower limit of integration]")
        sys.exit(1)

    # default lower bound
    a = 0
    
    # default upper bound
    b = 10
    
    # default number of sub intervals
    Nint = 1
   
    # read the user-provided input from the command line (if there)
    if '-Nint' in sys.argv:
        p = sys.argv.index('-Nint')
        Nint = sys.argv[p+1]
    if '-upper' in sys.argv:
        p = sys.argv.index('-upper')
        utemp = float(sys.argv[p+1])
        if utemp > 0:
            b = utemp
    if '-lower' in sys.argv:
        p = sys.argv.index('-lower')
        ltemp = int(sys.argv[p+1])
        if ltemp > 0:
            a = ltemp

    
    #Implement a Monte Carlo integration to a function in one or more dimensions. You are welcome to start with your code from HW #6 (but please copy to a new file, don't overwrite your HW #6 work)
    
    
    
    
    # Quantify the accuracy of your MC integral as a function of the number of sample points and compare with the accuracy of your deterministic methods from HW #6
    
    
    
    
    # Optional: Feel free to try to improve your accuracy/efficiency using importance sampling, stratification, or a change of variables - how much does this help?
