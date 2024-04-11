# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Quantitative Methods and Simulation                             #
# Miguel Marines                                                  #
# Activity: Run Test									          #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# ----------------------------------------------------------------#
#                          Run Test                               #
# ----------------------------------------------------------------#

# Libraries
import numpy as np
import random as rnd
import math
from random_number_generator import *

# # Inputs by the user
# print("\n")
# file_name = input("Enter the name of the file to obtain the numbers: ")

# # Obtain the numbers from a file
# # text_file = open("/Users/.../runs_data.txt", "r")
# text_file = open(file_name, "r")
# numbers = text_file.readlines()
# # print (numbers)
# # print (len(numbers))
# n = len(numbers)
# text_file.close()

new_numbers = gen_exp(10000,100)
n = 10000

# ----------------------------------------------------------------- #
# Clasify numbers according to the intervals and obtain frequencies #
# ----------------------------------------------------------------- #
positive = 0
negative = 0
signs = np.full((n), 0) # + = 0    |   - = 1
signs_char = np.full((n - 1), "s")

for i in range(n - 1):
    if(new_numbers[i] <= new_numbers[i+1]):
        positive = positive + 1
        signs[i] = 0
        signs_char[i] = "+"
    else:
        negative = negative + 1
        signs[i] = 1
        signs_char[i] = "-"


#-----------------------#
# Print Generated Signs #
#-----------------------#
print("\n")
p = int(input('If you want to print the generated signs press 0, otherwise press other number: '))

print("\n")
print('Generated Signs:')
if(p == 0):
    for i in range(n - 1):
        print(signs_char[i], end=" ")

print("\n")

total = positive + negative

print('(+): {:.{}f},'.format(positive, 0), '(-): {:.{}f}, '.format(negative, 0), 'Total: {:.{}f}'.format(total, 0))
print("\n")


#----------------------------#
# Positive and Negative Runs #
#----------------------------#
positive_runs = 1
negative_runs = 0
for i in range(n-1):
    if(signs[i] == 0 and signs[i+1] == 1):
        positive_runs = positive_runs + 1
    elif(signs[i] == 1 and signs[i+1] == 0):
        negative_runs = negative_runs +1

total_runs = positive_runs + negative_runs


#----------------------------------#
# Print Positive and Negative Runs #
#----------------------------------#
print("Positive Runs: %i" % positive_runs)
print("Negative Runs: %i" % negative_runs)
print("Total Runs: %i" % total_runs)
print("\n")


#----------------------------------#
#       Mius, Sigma and Zscore     #
#----------------------------------#
expected_value = ((2 * (n - 1)) - 1) / 3
standard_deviation = math.sqrt(((16 * (n - 1)) - 29) / 90)
z_score = (total_runs - expected_value) / standard_deviation

print("Statics")
print("Miu = %f" % expected_value)
print("Sigma = %f" % standard_deviation)
print("Zscore = %f" % z_score)

print("\n")

print("H0: Appereance of the numbers is random.")
print("H1: Appereance of the numbers is not random.")

if(z_score < 1.96):
    print("Since |%f| < |1.96|, H0 is not rejected." % z_score)
else:
    print("Since |%f| > |1.96|, H0 is rejected." % z_score)

print("\n")
