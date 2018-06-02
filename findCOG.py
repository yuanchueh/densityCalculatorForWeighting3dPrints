import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# print("hello")
n=20
x = np.random.randint(-50,50,n)
y = np.random.randint(0,200,n)
z = np.random.randint(0,30,n)
m = np.random.randint(1,200,n)
# print(m)
# y = np.zeros(len(m))
cgx = np.sum(x*m)/np.sum(m)
cgy = np.sum(y*m)/np.sum(m)
cgz = np.sum(z*m)/np.sum(m)
# print("The center of mass in x is {0:.4f}".format(cgx))

#1D
# plt.scatter(x,y,s=m)
# plt.scatter(cgx,0,color='k', marker='|', s=1e4)
# plt.gca().set_yticks([])
# plt.title('1 dimension COG')
# %matplotlib qt
#2D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.rcParams['figure.figsize'] = (6, 10)  # (width, height)
plt.scatter(x,y,s=m)

plt.
plt.scatter(cgx, cgy, color='k', marker='+', s=1e4)
plt.title('2 Dimensional Center of Gravity')
