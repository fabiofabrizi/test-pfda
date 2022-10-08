# import matplotlib
import matplotlib.pyplot as plt
# import numpy
import numpy as np

# range returns a list of numbers - range() only works with integers
#x = range()
x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x
# normal is the normal distribution, also known as Gaussian distribution
# The noise is centred at 0.0 and std dev is 1.0
# So mean is 0, with +/- 1.0 std dev, range of 10

noise = np.random.normal(0.0, 1.0, (len(x)))

plt.plot(x, y, 'b.')
plt.plot(x, noise, 'g-')
# Now add the noise to the graph:
plt.plot(x, y + noise, 'r-')
plt.ylabel('some numbers')

# Command below is called 'flushing the buffer'.
plt.show()