#!/opt/local/bin/python2.7

import random
import matplotlib.pyplot as plt
import numpy as np

# Generate random numbers for approxiamtion
NUM_POINTS = 10000
x = [random.uniform(0,1) for i in xrange(NUM_POINTS)]
y = [random.uniform(0,1) for i in xrange(NUM_POINTS)]

circle_x = []
circle_y = []
outsiders_x = []
outsiders_y = []
hits = 0

for i in xrange(NUM_POINTS):
    if x[i]**2 + y[i]**2 <= 1:
        circle_x.append(x[i])
        circle_y.append(y[i])
        hits += 1
    else:
        outsiders_x.append(x[i])
        outsiders_y.append(y[i])

# Approximating pi by
# Number of hits * 4 quaters / number of trials 
pi = float(hits) * 4 / NUM_POINTS 
print pi

# Plot 
plt.title('approximation of pi')
plt.scatter(outsiders_x, outsiders_y, s=1, color='blue')
plt.scatter(circle_x, circle_y, s=1, color='green')
plt.show()

