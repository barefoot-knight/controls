import numpy as np
import control
import matplotlib.pyplot as plt

kp = 1.5
Dc = kp
numD = kp
denD = 1
numG = 1
denG = [1,1.4,1]
sysD = control.tf(numD, denD)
sysG = control.tf(numG, denG)
TF = sysG*sysD/(1 + sysG*sysD)
t = np.arange(0,10,.01)
tout,yout = control.step_response(TF,t)
plt.plot(tout,yout, label = f"kp = {kp}")

kp = 6
Dc = kp
numD = kp
denD = 1
numG = 1
denG = [1,1.4,1]
sysD = control.tf(numD, denD)
sysG = control.tf(numG, denG)
TF = sysG*sysD/(1 + sysG*sysD)
t = np.arange(0,10,.01)
tout, yout = control.step_response(TF,t)
plt.plot(tout,yout, label = f"kp = {kp}")
plt.legend()
plt.show()