import numpy as np
import sys_info
import matplotlib.pyplot as plt
import control



t = np.arange(0,5,0.01)
y = 1-np.exp(-1.2*t)*(np.cos(1.6*t)+3/4*np.sin(1.6*t))

sys = sys_info.sys_info(t,y)
print(sys)
plt.plot(t,y)
plt.show()