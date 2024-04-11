# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Quantitative Methods and Simulation                             #
# Miguel Marines                                                  #
# Activity: Monte Carlo Simulation for Intigrals		          #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# ----------------------------------------------------------------#
#              Monte Carlo Simulation for Intigrals               #
# ----------------------------------------------------------------#

# Libraries
import numpy as np
import matplotlib.pyplot as plt

# Number of points.
N = int(input('N: '))

# Graph the function.
# Adjust axis according to the lower and upper limit.
axis = np.linspace(0.0001,3.2)
function =  1 / (1 + np.sinh(2 * axis) *(np.log(axis)) ** 2)

# Limits of the integral.
lower_limit = 0.8
upper_limit = 3

# Array of random numbers, according to the upper and lower limit of the integral.
array_random_numbers = np.random.uniform(lower_limit, upper_limit, N)

addition = 0

# Computation of the integral.
for i in range(N):
    addition = addition + ( 1 / (1 + (np.sinh(2 * array_random_numbers[i]) * (np.log(array_random_numbers[i])) ** 2)))
result = ((upper_limit - lower_limit) * addition) / N

# Graphing Axis
plt.xlabel('x')
plt.ylabel('f(x) = y')

# Graphing Function
plt.plot(axis,function)

# Graphing Rectangle
plt.hist(array_random_numbers, density = True)

# Prints the result of the integral.
print('Result of the Integral: ', result)

# Shows Graph
plt.show()