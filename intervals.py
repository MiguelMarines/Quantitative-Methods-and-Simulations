# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Quantitative Methods and Simulation                             #
# Miguel Marines                                                  #
# Activity: Grouping data with frequency tables.                  #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# File with Numbers
# Number Decimals

# N -> Total of Numbers
# C -> Number of Intervals
# Max -> Maximum Number
# Min -> Minimum Number
# W -> Interval Size

# Inteval Frequencies.
# Sum of Frequencies.


# Libraries
import matplotlib.pyplot as plt
import random
import math
import numpy
import numpy as np


# Inputs by the user.
file_name = input("Enter the name of the file to obtain the numbers: ")
nd = int(input("Enter the number of decimals: "))
# n = int(input("Enter the number of numbers: "))
# min = float(input("Enter the minum number: "))
# max = float(input("Enter the maximum number: "))


# Obtain the numbers from a file.
# text_file = open("/Users/.../data03.txt", "r")
text_file = open(file_name, "r")
numbers = text_file.readlines()
# print (numbers)
# print (len(numbers))
n = len(numbers)
text_file.close()

new_numbers = [float(nums) for nums in numbers]

maxi = np.max(new_numbers)
mini = np.min(new_numbers)


# Generate random numbers.
# numbers = numpy.random.uniform(min, max, n)

# Compute of C and W.
num_clases = int(round(float(1 + 3.33 * math.log10(n))))
w = float(((maxi - mini) / num_clases) + (1 / (10**nd)))


# Compute of intervals.
clases = []
interval_value  = mini
for i in range(num_clases):
    interval_value = interval_value + w
    clases += [interval_value]
    # print(clases[i])


frequencies = np.full((num_clases), 0)


# Clasify numbers according to the intervals and obtain frequencies.
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

# Obtain total frecuencies.
sum_frecuencies = 0
for i in range(num_clases):
    sum_frecuencies = sum_frecuencies + new_frequencies[i]


# Print the information.
print("\n")
print("N: %i" % n)
print("C = %i"  % num_clases)
print('Max: {:.{}f}'.format(maxi, nd))
print('Min: {:.{}f}'.format(mini, nd))
print('W = {:.{}f}'.format(w, nd))
print("\n")


interval_value2  = mini
preview_interval2 = 0


print("Intervals        Frequencies")
for i in range(num_clases):
    interval_value2 = interval_value2 + w
    preview_interval2 = interval_value2 - w
    # print ("[%.4f - %.4f)    %i" % (preview_interval2, interval_value2, new_frequencies[i]))
    print('[{:.{}f}'.format(preview_interval2, nd), '- {:.{}f})    '.format(interval_value2, nd), new_frequencies[i])

print("\n")
print("Sum of Frequencies: %i" % sum_frecuencies)


# Graphs the information
plt.figure(1)
plt.bar(clases, new_frequencies)
plt.title("Frequencies of Grouped Data")
plt.xlabel('Intervals')
plt.ylabel('Frequencies')
plt.show()
