import control
import numpy as np
import matplotlib.pyplot as plt
import control.matlab as matlab

# control.root_locus(control.tf((1),(1,1,0)))

num = [1,2.5]
den = np.convolve([1,1,0],[1,8,52])
G = control.tf(num,den)
ps = control.pole(G)
zs = control.zero(G)

# find departure angles
for i in range(len(ps)):
    dep=np.sum(np.angle(ps[i]-zs))-np.sum(np.angle(ps[i]-ps))-np.pi
    dep_d = np.mod(dep*180/np.pi,360)# trim to less than 2pi
    print('pole:', ps[i], 'dep angle:', dep_d)

#find arrival angles
for i in range(len(zs)):
    arr=np.sum(np.angle(zs[i]-ps))-np.sum(np.angle(zs[i]-zs))-np.pi
    arr_d = np.mod(arr*180/np.pi,360) # trim to less than 2pi
    print('zero:', zs[i], 'dep angle:', arr_d)
control.root_locus(G, plotstr=[],print_gain='on')
plt.grid()
plt.show()


'''print(den)
sysL = control.tf(num,den)
control.root_locus(sysL,print_gain='on')
plt.show()'''