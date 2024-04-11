# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Quantitative Methods and Simulation                             #
# Miguel Marines                                                  #
# Activity: Random Number Generator								  #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

import numpy as np
import random as rnd


#-------------------------------------------------------------------#

# def gen_func(N):
# 	R = np.random.rand(N)
# 	x = 3 ** (R) / 2
# 	return x

# Plot Customized P.D.F 
def gen_func(N):
	numbers = []
	for _ in range(N):
		R = rnd.random()
		numbers.append(3 ** (R) / 2) # Change to the corresponding P.D.F
	return numbers

#-------------------------------------------------------------------#


# def gen_exp(N, lam):
# 	#R = np.random.rand(N)
# 	R = LCG(N, 1, 2, 3, 20)
# 	x = -np.log(R) / lam
# 	return x

# Exponential Function
def gen_exp(N, lam):
	numbers = []
	for _ in range(N):
		R = rnd.random()
		x = -np.log(R) / lam
		numbers.append(x)
	return numbers

#-------------------------------------------------------------------#


# def gen_triangular(N, a, b, c):
# 	R = np.random.rand(N)
# 	cut = (c - a) / (b - a)
# 	x = np.piecewise(R, [R <= cut, R > cut], [lambda R: a + np.sqrt(R * (b - a) * (c - a)), lambda R: b - np.sqrt((1 - R) * (b - a) * (b - c))])
# 	return x

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

#-------------------------------------------------------------------#


def LCG(N, X0 = 123457, a = 16807, c = 0, m = 2 ** 31 - 1):
	R = np.empty(N)
	for i in range(N):
		X_next = (a * X0 + c) % m
		R[i] = X_next / m
		X0 = X_next
	return R
#-------------------------------------------------------------------#

def gen_weibull(N, alpha, beta):
    R = np.random.rand(N)
    x = alpha * (-np.log(R)) ** (1 / beta)
    return x 

#-------------------------------------------------------------------#


def gen_normal(N, miu, sigma):
    U1 = np.random.rand(N)
    U2 = np.random.rand(N)
    x = miu + sigma * np.sqrt(-2 * np.log(U1)) * np.cos(2 * np.pi * U2)
    return x

#-------------------------------------------------------------------#


#np.savetxt('numbers.txt', numbers)
numbers = np.loadtxt('/Users/.../numbers01-1.txt')
