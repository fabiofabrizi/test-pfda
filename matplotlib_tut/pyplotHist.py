# In this file we're looking at how to plot histograms
import matplotlib.pyplot as plt
import numpy as np

# random is a method built-in to numpy
# normal() is the normal distribution
# So below is centred around 0.0, std dev of 1.0 and 1000 points
x = np.random.normal(0.0, 1.0, 100000)

# The below doesn't show the bell curve.
#plt.plot(x)

# Use the below to show the bell curve - a histogram.
# NB the number of bins will total the last parameter above (100000 in this case)
plt.hist(x, bins = 80)
plt.show()