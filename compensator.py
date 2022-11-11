import control
import numpy as np
import matplotlib.pyplot as plt
from sys_info import *

G = control.tf((1), (1,1,0))
Le = control.tf((1,2),(1,13))
K = 70
tf = K*Le*G
print(tf)




control.root_locus(tf/K,plotstr=[])
plt.ylim([-8,8])
plt.grid()


plt.figure(2)
## feedback system response
sys = control.feedback(tf)
print(sys)
t = np.arange(0,10,.01)
y = control.step_response(sys, t)
plt.plot(t,y[1])
plt.grid()


print(sys_info(t, y[1]))

s = np.complex(-4.3,6.4)
print(np.abs(control.evalfr(Le*G,s)))

plt.show()

