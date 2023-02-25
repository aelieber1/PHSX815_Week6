"""
Purpose: Homework #6 PHSX 815
University of Kansas

author: @aelieber1 + several sources cited throughout code
"""

# Import necessary functions
import scipy.integrate as spi
import numpy as np


""" 
Function definition on a closed interval that is not a low order polynomial, but whose integral can still be calculated analytically 

Credit: 
- utilizes code from this integrals in python website: 
https://computationalmindset.com/en/mathematics/integral-calculus-in-python.html
- scipy.integrate documentation: 
https://docs.scipy.org/doc/scipy/tutorial/integrate.html
"""

print('Integral of 4xe^-x from x=1 to x=5')

# integral definition
integrand = lambda x : 4 * x * np.exp(-x)
a = 1. # lower bound
b = 5. # upper bound

# calculation of the integral analytically using scipy
# utilizes scipy.quad which is general purpose integration in scipy literature
result, error = spi.quad(integrand, a, b)
print('Result is ', result, 'with error ', error)

"""
Implement two different numerical integration methods to integrate this function (don't need to be of very high order)
1. fixed interval sizes
2. Gaussian quandrature
* write code such that you can cahnge the number of sub intervals and number of evaluation points -- TODO: do cmd line input as earlier
"""


"""
1. Compare the difference between the two numerical integrals
2. Compare the difference with the correct/analytical answer
* both as functions of the number of sub intervals

Answer: Is the difference between the two estimates a good indicator of the actual error? 
"""