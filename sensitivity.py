## Sensitivity
import control
import control.matlab as ctrl
import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0,10,.01) 
n = len(t)

# System 
den = [1,60]
G=control.tf(600,den)
#print(G)
print(control.tf([1],[1,0]))
Kp = 0.1
Ki = 12
DcPI= (Kp + Ki*control.tf([1],[1,0])) # controller  
sysPI = DcPI*G/(1+DcPI*G) # closed loop TR 
yPI = control.step_response(sysPI*control.tf([1],[1,0]),t) # step response  
'''Ss = control.minreal(1/(1+DcPI*G))
print(Ss)
R = control.tf((1),(1,0,0))
print(R)
s = control.tf([1,0],[1])
e_ss = control.minreal(s*R*Ss)
print(e_ss)
print(control.evalfr(e_ss,0))
'''

#System type - PI 
sysS = control.minreal(1/(1+DcPI*G)) #sensitivity 
print(sysS) 
zeros = control.zero(sysS) #zeros in sensitivity 
sysType = len(zeros)-np.count_nonzero(zeros) #system type by zeros at origin 
# Input type for checking system error 
sysR=np.zeros(sysType+1); #check error 
sysR[0] = 1; 
sysR=control.tf(1,sysR) 
essPI=control.evalfr(control.minreal(sysS*sysR),0) 
print('System type =' , sysType,'ess = ', essPI)

plt.plot(t,yPI[1], 'green')
plt.plot(t,t)
plt.grid('on') 
plt.xlabel('time (s)') 
plt.ylabel('y(t)') 
ref = t
y = control.matlab.lsim(sysPI,ref,t)
plt.plot(t,y[0])
#plt.xlim(0, 2);plt.ylim(0, .5)
plt.show()
