# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Quantitative Methods and Simulation                             #
# Miguel Marines                                                  #
# Activity: Histograms					                    	  #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

import numpy as np
import matplotlib.pyplot as plt
from list_of_numbers import *

def trunc_dec(num, d):
	return np.trunc(num * (10 ** d)) * (10 ** - d)

def trunc_add_dec(num, d):
	return np.trunc(num * (10 ** d)) * (10 ** - d) + 10 ** - d

d = 4

numbers = np.round(numbers, d)
#print(numbers)
N = len(numbers)
print(f'N: {N}')
Cs = np.round(1 + 3.33*np.log10(len(numbers)), 0)
C = int(input(f'C (Press 0 for suggested {Cs}): '))

if C == 0:
	C = Cs

print(f'C = {C:.0f}')

biggest = np.max(numbers)
smallest = np.min(numbers)

print(f'Max: {biggest:.{d}f}, min: {smallest:.{d}f}')

W = ((biggest - smallest) / C)
Ws = trunc_add_dec(W, d)

W = float(input( f'W (Press 0 for suggested {Ws:.{d}f}): '))

if W == 0:
	W = Ws

print(f'W = {W:.{d}f}')

hist = {}

inf = smallest
sp = 2 * d + 15

intervals_str = 'Intervals'
freq_str = 'f'

print(f'\n{intervals_str: <{sp}}{freq_str}')

for i in range(int(C)):
	sup = np.round(inf + W, d)
	#sup = np.round(inf + W - 1 / (10 ** d), d)
	hist[f'I{i + 1}'] = [inf, sup, 0]
	#inf = np.round(sup + 1 / (10 ** d), d)
	inf = sup


# print(hist)
i = 0
total = 0

missing_n = set()

for num in numbers:
	num_added = False
	for interval in hist:
		if hist[interval][0] <= num < hist[interval][1]:
			hist[interval][2] += 1
			total += 1
			num_added = True
			break
	if num_added == False:
		missing_n.add(num)


labels_inter = []
labels_freq = []

for interval in hist:
	#inter_str = f'{hist[interval][0]:.{d}f} - {hist[interval][1]:.{d}f}'
	inter_str = f'[{hist[interval][0]} - {hist[interval][1]})'
	labels_inter.append(inter_str)
	print(f'{inter_str:<{sp}}{hist[interval][2]:.0f}')
	labels_freq.append(hist[interval][2])

print(f'\nSum of requencies: {total}')


#plt.plot(labels_inter, labels_freq, 'b')
plt.bar(labels_inter, labels_freq)
plt.title('Frequencies of grouped data')
plt.xlabel('Bins')
plt.ylabel('Frequencies')
plt.show()

print('***')
print(f'Avg: {np.mean(numbers)}')
#print(missing_n)
