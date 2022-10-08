# This is looking at titles, labels and legends.

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

plt.plot(x, y + noise, 'g.', label='Actual Data')
plt.plot(x, y, 'b-', label='Fitted Model')


# Titles, labels - Remember to include units!
plt.title("Average speed vs distance covered over time.")
plt.xlabel("Average speed km/h")
plt.ylabel("Distance covered (km)")
plt.legend()

# Command below is called 'flushing the buffer'.
plt.show()