# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Quantitative Methods and Simulation                             #
# Miguel Marines                                                  #
# Activity: Histograms							                  #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

'''
obtain_parameters(numbers, d) -> return C, W, smallest
make_table(numbers, C, W, smallest) -> return hist, sum_freq
print_histogram(numbers, hist, d, total)
plot_histogram(hist, d)

generate_histogram(numbers, dec = 4, plot_h = True) -> return hist
'''

import numpy as np
import matplotlib.pyplot as plt
from random_number_generator import *


def trunc_dec(num, d):
	return np.trunc(num * (10 ** d)) * (10 ** - d)

def trunc_add_dec(num, d):
	return np.trunc(num * (10 ** d)) * (10 ** - d) + 10 ** - d

def obtain_parameters(numbers, d):
	N = len(numbers)
	print(f'N: {N}')
	Cs = np.round(1 + 3.33 * np.log10(len(numbers)), 0)
	C = int(input(f'C (Press 0 for suggested {Cs:.0f}): '))
	if C == 0:
		C = Cs
	print(f'C = {C:.0f}')

	biggest = np.max(numbers)
	smallest = np.min(numbers)
	print(f'Max: {biggest:.{d}f}, min: {smallest:.{d}f}')
	W = ((biggest - smallest) / C)
	Ws = trunc_add_dec(W, d)

	W = float(input(f'W (Press 0 for suggested {Ws:.{d}f}): '))
	if W == 0:
		W = Ws
	print(f'W = {W:.{d}f}')

	return C, W, smallest



def make_table(numbers, C, W, smallest):
	# Dictionary representing the histogram with the following structure.
	hist = {}
	inf = smallest

	# Initialize dictonary with intervals and bounds. Frequencies are zero.
	for i in range(int(C)):
		# sup = np.round(inf + W, d)
		sup = inf + W
		hist[f'I{i + 1}'] = [inf, sup, 0]
		inf = sup

	sum_freq = 0
	# Set that stores missing values. Sets doesn´t store repeated values.
	missing_n = set()

	# Loop every number and find the fitting interval.
	for num in numbers:
		num_added = False # Flag for missing numbers.
		for interval in hist:
			if hist[interval][0] <= num < hist[interval][1]: # Semiopen interval [inf, sup)
				hist[interval][2] += 1
				num_added = True
				break # If the fitting interval was found, go to the next number.
		if num_added == False:
			missing_n.add(num)

	print(f'Missing numbers: {missing_n}')

	return hist, sum_freq


def print_histogram(numbers, hist, d, total):
	sp = 2 * d + 15 # Spaces for printing purposes.
	intervals_str = 'Intervals'
	freq_str = 'f'
	print(f'\n{intervals_str: <{sp}}{freq_str}') # <sp means align to the left.
	for interval in hist:
		inter_str = f'[{hist[interval][0]:.{d}f} - {hist[interval][1]:.{d}f})' # Current interval as string.
		print(f'{inter_str:<{sp}}{hist[interval][2]:.0f}') # Print interval and frequency.
		total = total + hist[interval][2]
	
	print(f'\nSum of Frequencies: {total}')
	print(f'Avg: {np.mean(numbers):.{d}f}')


def plot_histogram(hist, d):
	labels_inter = []
	labels_freq = []
	# Creates the bins labels for the histogram.
	for interval in hist:
		inter_str = f'[{hist[interval][0]:.{d}f} - {hist[interval][1]:.{d}f})'
		labels_inter.append(inter_str)
		labels_freq.append(hist[interval][2])
	
	plt.bar(labels_inter, labels_freq)
	plt.title('Frequencies of Grouped Data')
	plt.xlabel('Bins')
	plt.ylabel('Frequencies')
	print('***')
	plt.show()


def generate_histogram(numbers, dec = 1, plot_h = True):
	#numbers = trunc_dec(numbers, d)
	#print(numbers)

	C, W, smallest = obtain_parameters(numbers, dec)
	hist, sum_freq = make_table(numbers, C, W, smallest)
	print_histogram(numbers, hist, dec, sum_freq)

	if plot_h == True:
		plot_histogram(hist, dec)
	return hist





# N = 1000
# numbers = gen_triangular(N, 0, 1, 0.5)
# numbers = gen_normal(N, 50, 20)
# numbers = gen_weibull(10000, 1, 5)
# numbers = gen_normal(N, 50, 20)
# numbers = gen_exp(N,10)
# numbers = gen_func(N)
generate_histogram(numbers, 4)
