# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Quantitative Methods and Simulation                             #
# Miguel Marines                                                  #
# Activity: LCG									                  #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

#-------------------------------------------------------------------#
#								LCG									#
#-------------------------------------------------------------------#

import numpy as np
import random as rnd

def LCG(N, X0, a, c, m):
	R = np.empty(N)
	for i in range(N):
		X_next = ((a * X0) + c) % m
		R[i] = X_next / m
		X0 = X_next
	return R

print("\n")
n = int(input("Enter the value of N: "))
x0 = int(input("Enter the value of X0: "))
a = int(input("Enter the value of a: "))
c = int(input("Enter the value of c: "))
m = int(input("Enter the value of m: "))

# N = 10, X0 = 6, a = 32, c = 3, m = 80
numbers = LCG(n, x0, a, c, m)

print("\n")
print("LCG Generated Numbers:")
print(numbers)
print("\n")
