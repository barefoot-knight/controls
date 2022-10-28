import control
import numpy as np
import matplotlib.pyplot as plt
# control.root_locus(control.tf((1),(1,1,0)))
num = [1,1]
den = np.convolve([1,5,0],[1,4,8])
print(den)
sysL = control.tf(num,den)
control.root_locus(sysL,print_gain='on')
plt.show()