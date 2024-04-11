# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Quantitative Methods and Simulation                             #
# Miguel Marines                                                  #
# Activity: Numbers List				                    	  #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

import numpy as np
import random as rnd

N = 1000
L = 10


# Triangular Function
def gen_triangular(N, a, b, c):
	numbers = []
	for _ in range(N):
		R = rnd.random()
		cut = (c - a) / (b - a)

		if 0 <= R <= cut:
			x = a + np.sqrt(R * (b - a) * (c - a))
		else:
			x = b - np.sqrt((1 - R) * (b - a) * (b - c))
		numbers.append(x)
	return numbers


# Exponential Function
def gen_exp(N, lam):
	numbers = []
	for _ in range(N):
		R = rnd.random()
		x = -np.log(R) / lam
		numbers.append(x)
	return numbers


# Plot customized P.D.F 
def gen_func(N):
	numbers = []
	for _ in range(N):
		R = rnd.random()
		numbers.append(3**(R)/2) # Change to the corresponding P.D.F
	return numbers


# numbers = gen_func(N)
numbers = gen_exp(N, L)
numbers = gen_triangular(N, 10, 80, 30)
# print(numbers)
# numbers = np.loadtxt('/Users/.../data03.txt')
