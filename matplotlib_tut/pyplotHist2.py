# In this file we're looking at how to plot two plots side by side

import matplotlib.pyplot as plt
import numpy as np

# random is a method built-in to numpy
# normal() is the normal distribution
# So below is centred around 0.0, std dev of 1.0 and 1000 points
x = np.random.normal(0.0, 1.0, 100000)
# First number is number of cols in sub plot
# Second number is number or rows in sub plot
# Third number is index of where you want to put rows to start
plt.subplot(1, 2, 1)
plt.hist(x, bins = 80)

"""
    The definition of uniform distribution is that it has as much likelihood of generating
    values in the lower bound as the upper bound, i.e. the numbers are distributed 'uniformly' 
    across the range.
"""


# Lower bound of data is -4.0
# Upper bound of data is 3.0
# Between the lower and upper bounds, generate 1000 data points.
x = np.random.uniform(-4.0, 3.0, 1000)
plt.subplot(1, 2, 2)
plt.hist(x)


plt.show()