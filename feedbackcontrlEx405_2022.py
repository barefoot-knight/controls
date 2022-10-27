# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 11:06:43 2022

# Model ramp input responses with lsim
# PI controller for a thermal unit
@author: Julia
"""

import control
import control.matlab as matlab
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

# Define the output time range
t=np.arange(0,30,.01)
# sys = GDc/(1+GDc)
# G=Ko/(T1*s+1)/(T2*s+1)
# Dc = Kp, Kp + KI/s
DcPI = .03 +.003*control.tf([1],[1,0])
DcP = 0.03
Ko = 1000; T1 = 1; T2 = 10
Ko = 1000; T1 = 1; T2 = 10
KP = .03; KIn = 0.003; KId=0; KD =0

# System

num = Ko
den = np.convolve([T1,1],[T2,1])
G = control.tf(num, den)
sysP = G*DcP/(1+DcP*G)
sysPI = G*DcPI/(1+DcPI*G)

# Simulation reference input u
n = len(t)
# input signal

# ramp functions with peak at t = 10 sec
# so, r(t) = 30*t - 30*tu(t-10) + 300u(t-10)
# ref = 30*t - (30*t - 300) * np.heaviside(t-10,1))
ref = 30*t
end = len(t)
ref[1000:end] = 300

# Declare teh state-space system and
# call matlab.lsim for both P and PI
sys_P = control.tf2ss(sysP)
yp = matlab.lsim(sysP,ref,t)
sys_PI = control.tf2ss(sysPI)
yPI = matlab.lsim(sysPI,ref,t)
print(sysP)
print(sysPI)

plt.plot(t,ref)
plt.show()