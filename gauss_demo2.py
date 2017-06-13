import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
rv = stats.multivariate_normal([0, 0], cov=1)

x, y = np.mgrid[-3:3:.15, -3:3:.15]
ax.plot_surface(x, y, rv.pdf(np.dstack((x, y))), rstride=1, cstride=1,cmap='rainbow')
ax.set_zlim(0, 0.2)

# savefig('../figures/plot3d_ex.png',dpi=48)
plt.show()
