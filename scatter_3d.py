from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

x_r = np.array([0, 1, 2, 3, 4, 5, 6])
y_r = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

x = x_r
for i in range(y_r.size - 1):
    x = np.append(x, x_r)

y = np.empty(x_r.size)
y.fill(0)
for i in range(y_r.size - 1):
    yy = np.empty(x_r.size)
    yy.fill(i+1)
    y = np.append(y, yy)

z_list = []
for i in range(y.size):
    z_list.append(x[i] + y[i])
z = np.array(z_list)        

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x, y, z, c='r')
ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')

plt.show()
