# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Quantitative Methods and Simulation                             #
# Miguel Marines                                                  #
# Activity: Poisson Random Numbers		                          #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# ----------------------------------------------------------------#
#                    Poisson Random Numbers                       #
# ----------------------------------------------------------------#

# Libraries
import numpy as np
import random as rnd
import math

#-----------------------------------------------------#
# Input by the user of alpha and numbers to generate  #
#-----------------------------------------------------#
print("\n")
alpha = float(input('Enter the value of alpha: '))
numbers_to_generate = int(input('How many numbers do you want to generate: '))
print("\n")

#-----------------------------------------------------#
#    Creates the array to store the random numbers.   #
#-----------------------------------------------------#
random_numbers = np.full((numbers_to_generate), 0.0000)

#-----------------------------------------------------#
#    Generates the random numbers and stores them.    #
#-----------------------------------------------------#
for i in range(numbers_to_generate):
    random_numbers[i] = rnd.uniform(0.0000,1.0000)
# print(random_numbers)

#random_numbers = [0.4357, 0.4146, 0.8353, 0.9952, 0.8004]
#random_numbers = [0.4357, 0.4146, 0.8353, 0.9952, 0.8004, 0.7945, 0.1530]

#-----------------------------------------------------#
#   Verify if the number satisfy the Possion Process  #
#-----------------------------------------------------#

n = 0
P = 1
N = 0

print("n     Rn+1      P            Accept/Reject        Result")

for i in range(numbers_to_generate):
    R = random_numbers[i]
    if(R < (math.e ** -alpha)):
        P = P * R
        N = n
        accept = "  P  < (e ^ -alpha) (Accept)"
        print(n,"   %.4f" % R, " ","%.4f" % P, accept, " N =", N)
        P = 1
        n = 0

    else:
        if(R >= (math.e ** -alpha)):
            P = P * R
            N = n
            if(P < (math.e ** -alpha)):
                accept = "  P  < (e ^ -alpha) (Accept)"
                print(n,"   %.4f" % R, " ","%.4f" % P, accept, " N =", N)
                P = 1
                n = 0
            else:
                reject = "  P >= (e ^ -alpha) (Reject)"
                print(n,"   %.4f" % R, " ","%.4f" % P, reject)
                n = n + 1
                N = n

print("\n")
