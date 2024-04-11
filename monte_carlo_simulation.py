# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Quantitative Methods and Simulation                             #
# Miguel Marines                                                  #
# Activity: Monte Carlo Simulation for Pi                    	  #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# ----------------------------------------------------------------#
#                 Monte Carlo Simulation for Pi                   #
# ----------------------------------------------------------------#
import numpy as np
import matplotlib.pyplot as plt

N = int(input('N: '))

blue_points = 0
theta = np.linspace(0, np.pi / 2, 200)
xc = np.cos(theta)
yc = np.sin(theta)

xb = []
yb = []
xr = []
yr = []

for _ in range(N):
    x = np.random.uniform(0,1)
    y = np.random.uniform(0,1)
    d = np.sqrt(x ** 2 + y ** 2)
    if d < 1:
        blue_points += 1
        xb.append(x)
        yb.append(y)
    else:
        xr.append(x)
        yr.append(y)

pi_app = 4 * blue_points / N
print(pi_app)

plt.plot(xc, yc)
plt.plot(xb, yb, 'ob')
plt.plot(xr, yr, 'xr')
plt.show()