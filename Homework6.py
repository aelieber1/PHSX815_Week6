"""
Purpose: Homework #6 PHSX 815
University of Kansas

author: @aelieber1 + several sources cited throughout code
"""

# Import necessary functions
import scipy.integrate as spi
import numpy as np
import sys
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
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

    """ 
    Function definition on a closed interval that is not a low order polynomial, but whose integral can still be calculated analytically 

    Credit: 
    - utilizes code from this integrals in python website: 
    https://computationalmindset.com/en/mathematics/integral-calculus-in-python.html
    - scipy.integrate documentation: 
    https://docs.scipy.org/doc/scipy/tutorial/integrate.html
    """
    print(a)
    print(b)
    # Analytical calculation of integral
    def f(x):
        return 4 * x * np.exp(-x)

    def f_prime(x):
        return 4 * (-x - 1) * np.exp(-x)

    # Evaluate integral
    upper_calc = f_prime(b)
    lower_calc = f_prime(a)
    analyt_int = upper_calc - lower_calc 

    print('Analytical Calculation of Integral of 4xe^-x from x=1 to x=10: ', analyt_int)

    # plot function
    x = np.linspace(0, 11, 100)
    plt.plot(x, f(x), color='red')
    #plt.show()


    """
    Implement two different numerical integration methods to integrate this function (don't need to be of very high order)
    1. fixed interval sizes
    2. Gaussian quandrature
    * write code such that you can change the number of sub intervals and number of evaluation points -- TODO: do cmd line input as earlier (check)
    """

    # calculation of the integral with fixed interval size
    funct = lambda x: 4 * x * np.exp(-x)
    # using scipy.integrate.romberg()
    result_romb = spi.romberg(f, 0, 10, show = True)

    print("The numerical result using Romberg's method with evenly space sub-intervals is {:f} (+-{:g})"
        .format(result_romb, a))

    # calculation of integral using Gaussian quadrature
    result_gaus, error_gaus = spi.quadrature(f, a, b)
    print("The numerical result using Gaussian Quadrature is {:f} (+-{:g})"
        .format(result_gaus, error_gaus))


    """
    1. Compare the difference between the two numerical integrals
    2. Compare the difference with the correct/analytical answer
    * both as functions of the number of sub intervals

    Answer: Is the difference between the two estimates a good indicator of the actual error? 
    """
    
    # Difference in the two numerical integrals
    numerical_difference = abs(result_romb - result_gaus)
    print('Difference betweent the two numerical integrals: ', numerical_difference)
    
    # Comparison of Numerical Integrals to the Correct Analytical Answer
    def percent (t, u):
        result = abs(float(((u - t) * 100) / t))
        return result
    
    print("Percent difference between romb and correct integral: ", percent(result_romb, analyt_int), "%")
    print("Percent difference between gaus quad and correct integral: ", percent(result_gaus, analyt_int), "%")