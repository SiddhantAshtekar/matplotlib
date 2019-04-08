import matplotlib.pyplot as plt
import numpy as np

x,y=np.loadtxt('example.txt',delimiter=',',unpack=True)
plt.plot(x,y,label='loaded from file using numpy@!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('numpy')
plt.legend()
plt.show()