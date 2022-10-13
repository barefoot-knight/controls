# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 13:30:25 2022
function: sys_info
@author: Julia
"""


import numpy as np

def sys_info(t,yout):
    
    tr = 0;
    tr1 = []
    tr2 = []
    
    os = max(yout-yout[0]) #max peak or overshoot
    ost = np.argmax(yout-yout[0]) # find the maximum peak time
    n = len(yout)
    
    if os > 0.9:
        tr1 = np.where(yout-yout[0] > 0.1); 
        tr2 = np.where(yout-yout[0] > 0.9); 
    else:
        tr1 = np.where(yout-yout[0] > 0.1*os); 
        tr2 = np.where(yout-yout[0] > 0.9*os); 
    tr2 = np.concatenate(tr2)
    tr1 = np.concatenate(tr1)
    if len(tr1) > 0:
        tr = (tr2[0]-tr1[0])*(t[1]-t[0])
    ts = np.argmin(abs(yout[ost:n-1]-yout[n-1])); 
    ts = t[ts]
    return os, tr,ts