%matplotlib inline
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
import matplotlib.pyplot as plt

# https://scicomp.stackexchange.com/questions/19807/solving-a-linear-equation-system-with-pure-neumann-condition
N = 40
nx = ny = N
D = np.zeros([nx, ny])
D[nx // 2, ny // 2] = 1
D[nx - N // 4, nx - N // 4] = 1
#print(nx, ny)
#print(np.mean(D))

nK = (nx - 2) * (ny - 2) + 1
A = np.zeros([nK, nK])
y = np.zeros(nK)
k = 0
for j in range(1, ny - 1):
  for i in range(1, nx - 1):
    if i == 1 and j == 1:
      A[k, k] = 1.
      A[k + 1, k] = -.5
      A[k + (nx - 2), k] = -.5
    elif i == nx - 2 and j == 1:
      A[k, k] = 1.
      A[k - 1, k] = -.5
      A[k + (nx - 2), k] = -.5
    elif i == 1 and j == ny - 2:
      A[k, k] = 1.
      A[k + 1, k] = -.5
      A[k - (nx - 2), k] = -.5
    elif i == nx - 2 and j == ny - 2:
      A[k, k] = 1.
      A[k - 1, k] = -.5
      A[k - (nx - 2), k] = -.5
    elif i == 1:
      A[k, k] = 2.
      A[k + 1, k] = -1.
      A[k + (nx - 2), k] = -.5
      A[k - (nx - 2), k] = -.5
    elif i == nx - 2:
      A[k, k] = 2.
      A[k - 1, k] = -1.
      A[k + (nx - 2), k] = -.5
      A[k - (nx - 2), k] = -.5
    elif j == 1:
      A[k, k] = 2.
      A[k - 1, k] = -.5
      A[k + 1, k] = -.5
      A[k + (nx - 2), k] = -1.
    elif j == ny - 2:
      A[k, k] = 2.
      A[k - 1, k] = -.5
      A[k + 1, k] = -.5
      A[k - (nx - 2), k] = -1.
    else:
      A[k, k] = 4.
      A[k - 1, k] = -1.
      A[k + 1, k] = -1.
      A[k + (nx - 2), k] = -1.
      A[k - (nx - 2), k] = -1.
      y[k] = D[i, j]

    k += 1

A[:, nK - 1] = 1.
A[nK - 1, :] = 1.
A[nK - 1, nK - 1] = 0
y[nK - 1] = 0

#print(A.T)
#print(y)
gx, gy = np.meshgrid(np.linspace(0, 1, nx - 2), np.linspace(0, 1, ny - 2))
x = np.linalg.solve(A, y)
x = x[:-1].reshape(nx - 2, ny - 2)

ax = plt.axes(projection='3d')
ax.plot_surface(gx, gy, x, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
