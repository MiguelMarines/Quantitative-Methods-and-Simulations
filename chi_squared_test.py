# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Quantitative Methods and Simulation                             #
# Miguel Marines                                                  #
# Activity: Chi Squared Test									  #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# ----------------------------------------------------------------#
#                         Chi-Squared Test                        #
# ----------------------------------------------------------------#

# Libraries
import numpy as np
import random as rnd
from random_number_generator import *

# Inputs by the user
print("\n")
# file_name = input("Enter the name of the file to obtain the numbers: ")
number_decimals = int(input("Enter the number of decimals: "))

# # Obtain the numbers from a file
# text_file = open("/Users/.../chi_data.txt", "r")
# text_file = open(file_name, "r")
# numbers = text_file.readlines()
# # print (numbers)
# # print (len(numbers))
# n = len(numbers)
# text_file.close()

new_numbers = LCG(1000, 11, 97, 3, 7411)
n = 1000

maxi = np.max(new_numbers)
mini = np.min(new_numbers)


# -------------------#
# Compute of C and W #
# -------------------#
num_clases = 10
w = 0.1

# ----------------------------------------- #
#           Compute of Intervals            #
# ----------------------------------------- #
clases = []
interval_value  = 0
for i in range(num_clases):
    interval_value = interval_value + w
    clases += [interval_value]
    # print(clases[i])

# ----------------------------------------------------------------- #
# Clasify numbers according to the intervals and obtain frequencies #
# ----------------------------------------------------------------- #
frequencies = np.full((num_clases), 0)

for i in range(n):
    for j in range(num_clases):
        if new_numbers[i] < clases[j]:
            frequencies[j] += 1
        else:
            frequencies[j] += 0

    j = 0


new_frequencies = np.full((num_clases), 0)
helper = 0
for i in range(num_clases):
    new_frequencies[i] = frequencies[i] - helper
    helper = frequencies[i]


# Obtain total frecuencies
sum_frecuencies = 0
for i in range(num_clases):
    sum_frecuencies = sum_frecuencies + new_frequencies[i]


# --------------------------------------------------------------- #
#                   Expected, X^2 and (O-E)^2 / E                 #
# --------------------------------------------------------------- #

expected_values = np.full((num_clases), 0)
for i in range(num_clases):
    expected_values[i] = n / num_clases

x02 = 0
x02s = np.full((num_clases), 0)

expected_values = expected_values.astype(float)
x02s = x02s.astype(float)

for i in range(num_clases):
    x02s[i] = ((new_frequencies[i] - expected_values[i]) ** 2)/ expected_values[i]
    #print(x02s[i])
    x02 = x02 + x02s[i]


# --------------------------------------------------------------- #
#                      Print Information                          #
# --------------------------------------------------------------- #

print("\n")
print("N = %i" % n)
print('Max = {:.{}f}'.format(maxi, number_decimals))
print('Min = {:.{}f}'.format(mini, number_decimals))
print("C = %i"  % num_clases)
print('W = {:.{}f}'.format(w, number_decimals))
print("\n")


interval_value2  = 0
preview_interval2 = 0

print("Intervals           Observed     Expected       (O-E)^2/E")
for i in range(num_clases):
    interval_value2 = interval_value2 + w
    preview_interval2 = interval_value2 - w
    print('[{:.{}f}'.format(preview_interval2, number_decimals), '- {:.{}f})      '.format(interval_value2, number_decimals), new_frequencies[i], '        {:.{}f}'.format(expected_values[i], number_decimals), '         {:.{}f}'.format(x02s[i], number_decimals))

print("\n")
print('----------------------------------------------- χ^2 = {:.{}f}'.format(x02, number_decimals))
print("Sum of Frequencies: %i" % sum_frecuencies)
print("\n")

print("H0: Generated numbers are not different from the uniform distribution.")
print("H1: Generated numbers are different from the uniform distribution.")
print("\n")

if(x02 < 16.9190):
    print('Since {:.{}f}'.format(x02, number_decimals), ' <  16.91, H0 is accepted.')
else:
    print('Since {:.{}f}'.format(x02, number_decimals), ' >  16.91, H0 is rejected.')

print("\n")
print(new_numbers)
