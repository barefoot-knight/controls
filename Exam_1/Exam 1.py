import control
import numpy as np
import matplotlib.pyplot as plt

J = 500000
B = 20000
K = 400


num = K/J
dem = [1, B/J, K/J]

t = np.arange(0, 400, .01)
sys = control.tf(num,dem)
y = control.step_response(sys, t)

plt.plot(t, y[1])
plt.xlabel("time (s)")
plt.ylabel("position from start (degrees)")
plt.title("Exam 1 Question 1-3")
plt.grid()
plt.show()


