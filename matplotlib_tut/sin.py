# sinusoidal function?

import matplotlib.pyplot as plt
import numpy as np

# Below has a range of approx -6 to 6 (because of 2 * 3.14)
x = np.arange(-2.0 * np.pi, 2.0 * np.pi, 0.1)

plt.plot(x, np.sin(x), 'g.')
plt.plot(x, np.cos(x), 'b.')

plt.show()