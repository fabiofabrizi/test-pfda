# import matplotlib
import matplotlib.pyplot as plt

# call matplotlib
#plt.plot([1, 2, 3, 4]) # list or array 
# Below plots the squares. 'bo' ensures points are plotted.
plt.plot([1, 2, 3, 4], [1, 4, 9, 16],'b.') # b. is blue dots.
plt.ylabel('some numbers')

# Command below is called 'flushing the buffer'.
plt.show()