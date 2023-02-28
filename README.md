# PHSX815_Week6

## Instructions: 

### Homework 6
- Choose a function on a closed interval (the function *cannot* be a low order polynomial, but need not be too complicated). Choose a function that you can calculate the integral for analytically.

- Implement *two different* numerical integration methods, one with fixed interval sizes, one with Gaussian quadrature, to integrate this function. These don't need to be of very high order. You should write your code such that you can change the number of sub-intervals (and number of evaluation points).

- Compare the difference between the two numerical integrals, and their difference with the correct/analytic answer, as a function of the number sub-intervals. Is the difference between the two estimates a good indicator of the actual error?

### Homework 7
- Implement a Monte Carlo integration to a function in one or more dimensions. You are welcome to start with your code from HW #6 (but please copy to a new file, don't overwrite your HW #6 work)

- Quantify the accuracy of your MC integral as a function of the number of sample points and compare with the accuracy of your deterministic methods from HW #6

- (Not required) Feel free to try to improve your accuracy/efficiency using importance sampling, stratification, or a change of variables - how much does this help?

## How to Run
### Homework "#"6
The python file `Homework6.py`can be run from the command line by typing:

	<> python3 Homework6.py -Nint [Number of Sub-Intervals] -upper [upper limit of integration] -lower [lower limit of integration] 
    
For running purposes, the Jupyter file `Homework6_functiontesting.py` can be disregarded.

### Homework 7
