# ~~~
# This file is part of the PhD-thesis:
#
#           "Adaptive Reduced Basis Methods for Multiscale Problems
#               and Large-scale PDE-constrained Optimization"
#
# by: Tim Keil
#
#   https://github.com/TiKeil/Supplementary-Material-for-PhD-thesis
#
# Copyright 2019-2022 all developers. All rights reserved.
# License: Licensed as BSD 2-Clause License (http://opensource.org/licenses/BSD-2-Clause)
# Authors:
#   Tim Keil     
# ~~~

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
import matplotlib as mpl
import tikzplotlib
# mpl.rcParams['figure.figsize'] = (8.0, 6.0)
# mpl.rcParams['font.size'] = 12
# mpl.rcParams['savefig.dpi'] = 300
# mpl.rcParams['figure.subplot.bottom'] = .1 
N = 40

dims = np.array([
    3, 3, 3, 3, 3, 3, 3, 5, 7, 10, 12, 9, 7, 6, 6, 7, 7, 6, 6, 9, 8, 6, 6, 6, 6, 6, 6, 6, 7, 9, 9, 9, 6, 6, 6, 6, 6, 6, 6, 6, 3, 3, 3, 4, 6, 4, 6, 7, 8, 9, 12, 9, 8, 6, 6, 9, 9, 9, 6, 9, 8, 6, 6, 6, 6, 6, 6, 6, 9, 10, 12, 9, 6, 7, 6, 6, 6, 6, 6, 6, 3, 3, 3, 3, 4, 4, 5, 7, 8, 9, 12, 10, 6, 6, 7, 8, 9, 9, 6, 9, 8, 6, 6, 6, 6, 6, 6, 6, 9, 11, 12, 9, 6, 6, 6, 6, 6, 6, 6, 6, 3, 3, 3, 3, 4, 3, 3, 6, 8, 9, 12, 9, 7, 6, 6, 7, 6, 8, 6, 9, 9, 6, 6, 6, 6, 6, 6, 6, 9, 11, 12, 9, 6, 6, 6, 6, 6, 6, 6, 6, 3, 4, 3, 3, 6, 4, 6, 6, 8, 9, 12, 9, 6, 6, 9, 8, 7, 7, 7, 9, 7, 6, 6, 6, 7, 6, 6, 6, 8, 11, 12, 9, 6, 6, 6, 6, 6, 6, 6, 6, 4, 5, 6, 5, 6, 3, 4, 6, 8, 9, 12, 9, 8, 6, 6, 7, 6, 8, 7, 9, 7, 6, 6, 6, 6, 6, 6, 6, 8, 9, 12, 9, 6, 6, 6, 6, 6, 6, 6, 6, 3, 3, 3, 3, 3, 6, 3, 6, 8, 9, 12, 9, 7, 7, 6, 6, 8, 9, 9, 9, 9, 6, 6, 7, 6, 6, 6, 6, 9, 10, 12, 9, 6, 6, 6, 6, 6, 6, 6, 6, 3, 3, 3, 5, 6, 6, 3, 6, 8, 9, 12, 9, 9, 7, 6, 6, 9, 9, 9, 9, 9, 6, 6, 6, 6, 6, 6, 6, 9, 11, 12, 9, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 9, 10, 12, 11, 11, 10, 10, 10, 10, 11, 11, 11, 10, 9, 9, 9, 10, 9, 9, 9, 9, 12, 12, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 9, 9, 9, 9, 9, 9, 9, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 11, 11, 11, 11, 12, 11, 12, 12, 12, 12, 11, 9, 9, 10, 9, 9, 11, 9, 9, 9, 9, 9, 9, 9, 9, 9, 11, 12, 12, 12, 11, 9, 9, 10, 9, 12, 12, 12, 12, 12, 9, 9, 9, 9, 9, 9, 10, 12, 12, 12, 11, 11, 10, 12, 11, 10, 12, 9, 6, 6, 6, 6, 6, 6, 6, 6, 7, 12, 12, 8, 6, 6, 6, 6, 6, 6, 7, 12, 11, 8, 6, 7, 6, 7, 6, 8, 8, 10, 12, 9, 9, 9, 9, 9, 9, 9, 9, 9, 6, 6, 7, 6, 6, 6, 6, 6, 6, 12, 9, 6, 5, 4, 3, 3, 3, 5, 5, 6, 6, 5, 5, 6, 5, 6, 6, 6, 6, 8, 9, 9, 6, 7, 9, 7, 9, 9, 9, 9, 6, 6, 6, 6, 6, 6, 6, 6, 6, 12, 9, 6, 3, 3, 3, 3, 3, 3, 5, 6, 6, 5, 3, 3, 3, 4, 4, 3, 3, 7, 9, 9, 9, 9, 8, 9, 9, 9, 9, 8, 6, 6, 6, 6, 6, 6, 6, 6, 6, 12, 9, 6, 3, 3, 3, 3, 3, 3, 5, 6, 6, 5, 3, 4, 3, 3, 3, 3, 3, 7, 9, 9, 6, 9, 9, 7, 9, 6, 6, 6, 6, 6, 6, 6, 6, 7, 6, 6, 6, 12, 9, 6, 3, 3, 3, 3, 3, 3, 5, 6, 6, 5, 3, 3, 3, 3, 3, 3, 4, 7, 9, 7, 8, 9, 9, 9, 9, 6, 6, 6, 7, 6, 6, 6, 6, 6, 6, 6, 6, 12, 9, 6, 3, 3, 3, 3, 3, 3, 5, 6, 6, 5, 3, 3, 3, 3, 3, 3, 3, 7, 9, 7, 6, 6, 6, 7, 9, 6, 6, 8, 6, 6, 7, 6, 6, 6, 6, 7, 6, 12, 9, 6, 3, 3, 3, 3, 3, 3, 5, 6, 6, 5, 3, 4, 3, 3, 3, 3, 5, 7, 9, 9, 9, 9, 6, 8, 7, 8, 9, 9, 6, 6, 6, 6, 6, 6, 7, 8, 8, 12, 9, 6, 3, 3, 3, 3, 3, 3, 5, 6, 7, 5, 3, 3, 3, 4, 3, 3, 4, 10, 11, 9, 9, 9, 9, 9, 9, 9, 9, 8, 9, 9, 9, 9, 9, 9, 9, 9, 11, 12, 12, 9, 7, 7, 6, 7, 6, 7, 6, 9, 9, 8, 6, 7, 9, 7, 6, 7, 10, 12, 12, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 11, 12, 12, 9, 6, 6, 7, 6, 6, 7, 7, 9, 9, 8, 9, 9, 8, 6, 9, 8, 12, 12, 12, 12, 9, 10, 9, 10, 11, 10, 9, 9, 7, 9, 9, 9, 10, 10, 9, 10, 10, 12, 11, 7, 6, 6, 4, 6, 6, 5, 3, 6, 6, 3, 5, 3, 3, 3, 5, 5, 9, 9, 9, 11, 10, 10, 10, 9, 9, 9, 9, 9, 7, 6, 6, 6, 6, 6, 8, 6, 8, 9, 7, 5, 6, 3, 4, 5, 3, 4, 3, 6, 6, 6, 5, 3, 3, 5, 3, 3, 8, 9, 11, 10, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 6, 9, 11, 5, 4, 3, 6, 3, 3, 6, 5, 6, 6, 4, 5, 3, 3, 3, 5, 4, 5, 9, 12, 9, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8, 7, 8, 9, 10, 6, 4, 4, 3, 4, 5, 3, 6, 6, 6, 4, 5, 5, 3, 3, 3, 3, 9, 9, 12, 8, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 6, 10, 8, 6, 6, 6, 4, 4, 3, 5, 6, 6, 6, 3, 4, 3, 3, 3, 5, 6, 8, 9, 9, 9, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 6, 6, 11, 11, 6, 3, 4, 6, 6, 3, 5, 5, 6, 6, 3, 3, 3, 3, 4, 3, 5, 9, 9, 10, 9, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8, 7, 6, 9, 10, 6, 4, 5, 3, 3, 3, 5, 3, 6, 6, 4, 3, 3, 3, 3, 3, 5, 8, 9, 11, 8, 7, 6, 7, 6, 7, 6, 6, 6, 7, 8, 8, 8, 9, 9, 9, 9, 9, 12, 11, 6, 7, 7, 5, 6, 6, 6, 6, 9, 7, 6, 5, 5, 5, 6, 6, 5, 9, 9, 9, 11, 9, 10, 9, 9, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 12, 12, 6, 9, 9, 9, 9, 9, 9, 9, 12, 12, 7, 6, 6, 6, 6, 6, 6, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 11, 9, 9, 9, 9, 9, 9, 9, 9, 9, 12, 12, 7, 6, 6, 6, 7, 7, 6, 6, 12, 12, 12, 9, 10, 9, 9, 9, 9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 9, 6, 6, 6, 5, 7, 6, 6, 6, 10, 12, 9, 9, 9, 9, 9, 9, 9, 9, 12, 10, 9, 10, 9, 8, 9, 9, 9, 9, 9, 6, 6, 6, 6, 6, 6, 6, 6, 9, 9, 9, 6, 7, 7, 6, 7, 7, 6, 6, 9, 9, 8, 7, 6, 7, 7, 6, 6, 8, 9, 9, 9, 6, 9, 7, 6, 6, 7, 7, 6, 7, 6, 6, 6, 6, 6, 6, 6, 9, 9, 9, 6, 5, 7, 6, 6, 7, 6, 6, 9, 9, 9, 7, 6, 6, 6, 7, 6, 8, 9, 9, 7, 6, 6, 6, 6, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 9, 9, 9, 6, 7, 6, 6, 6, 6, 6, 6, 9, 9, 9, 6, 7, 7, 6, 6, 6, 8, 9, 9, 6, 6, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 9, 9, 9, 6, 7, 6, 6, 6, 7, 6, 6, 9, 9, 7, 6, 7, 7, 6, 6, 6, 8, 9, 9, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 9, 9, 9, 6, 6, 7, 6, 6, 6, 6, 6, 9, 9, 7, 6, 6, 6, 6, 7, 7, 8, 9, 9, 6, 7, 7, 6, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 9, 9, 9, 6, 7, 6, 6, 6, 7, 6, 6, 9, 9, 8, 7, 7, 6, 7, 6, 6, 7, 9, 9, 6, 7, 7, 6, 6, 6, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 9, 9, 9, 6, 6, 6, 6, 6, 7, 6, 6, 9, 9, 8, 7, 7, 7, 7, 7, 6, 8, 9, 9, 6, 6, 6, 6, 6, 6, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 9, 9, 7, 6, 7, 7, 6, 6, 6, 6, 6, 9, 9, 8, 6, 7, 6, 6, 6, 7, 7, 9, 9, 7, 5, 6, 6, 6, 6, 6, 6, 6
])
dims_ = dims.reshape((N, N), order='F').T
subdomains = len(dims_)

min_size = np.min(dims)
max_size = np.max(dims)
print('sizes of the local reduced bases (min/max): {}/{}'.format(min_size, max_size))
# plt.matshow(dims_, cmap=cm.get_cmap('Purples', max_size - min_size + 1))
plt.imshow(dims_,
           origin='lower_left',
           interpolation='none', cmap=cm.get_cmap('Purples', max_size - min_size + 1),
           vmax=min_size, vmin=max_size)

ax = plt.gca();

# Major ticks
ax.set_xticks(np.arange(9, N, 10))
ax.set_yticks(np.arange(9, N, 10))

# Labels for major ticks
ax.set_xticklabels(np.arange(10, N+1, 10), fontsize=14)
ax.set_yticklabels(np.arange(10, N+1, 10), fontsize=14)

# Minor ticks
ax.set_xticks(np.arange(-.5, N, 1), minor=True)
ax.set_yticks(np.arange(-.5, N, 1), minor=True)

# Gridlines based on minor ticks
ax.grid(which='minor', color='k', linestyle='-', linewidth=0.5)

cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.tight_layout()

N = 40
plt.figure()
dims = np.array([
2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4,
       4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2,
       4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4,
       4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4,
       4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4,
       4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2,
       4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4,
       4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 4, 4,
       4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8,
       4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
       8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8,
       8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8,
       8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8,
       8, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8,
       4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4,
       4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8,
       8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4,
       4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8,
       8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
       4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4,
       8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 8,
       8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8,
       8, 8, 8, 8, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4,
       4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2,
       4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2,
       2, 2, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8,
       8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4, 4, 4,
       4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8,
       4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
       8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8,
       8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8,
       8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8,
       8, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8,
       4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4,
       4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8,
       8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4,
       4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8,
       8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
       4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4,
       8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 4, 4,
       4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4,
       4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4,
       4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4,
       2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4,
       8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4,
       4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8,
       8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4, 4, 4,
       4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8,
       4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
       8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8,
       8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8,
       8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8,
       8, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8,
       4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4,
       4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8,
       8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4,
       4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 8,
       8, 8, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2,
       2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2,
       4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4,
       4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4,
       4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4,
       4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2,
       4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4,
       4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4,
       2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2
])
dims_ = dims.reshape((N, N), order='F').T
subdomains = len(dims_)

min_size = np.min(dims)
max_size = np.max(dims)
print('sizes of the local reduced bases (min/max): {}/{}'.format(min_size, max_size))

# # patch 1
# p1 = [-0.5, 3.5]
# p2 = [3.5, 3.5]
# p3 = [3.5, -0.5]
# p4 = [-0.5, -0.5]
# plt.plot(p1, p2, color="red", linewidth=2)
# plt.plot(p4, p3, color="red", linewidth=4)
# plt.plot(p1, p4, color="red", linewidth=4)
# plt.plot(p2, p1, color="red", linewidth=2)

# patch 2
p1 = [6.5, 15.5]
p2 = [15.5, 15.5]
p3 = [15.5, 6.5]
p4 = [6.5, 6.5]
plt.plot(p1, p2, color="r", linewidth=2)
plt.plot(p4, p3, color="r", linewidth=2)
plt.plot(p1, p4, color="r", linewidth=2)
plt.plot(p2, p1, color="r", linewidth=2)
plt.imshow(dims_,
           origin='lower_left',
           interpolation='none', cmap=cm.get_cmap('Purples', max_size - min_size + 1),
           vmax=min_size, vmin=max_size)

ax = plt.gca();

# Major ticks
ax.set_xticks(np.arange(9, N, 10))
ax.set_yticks(np.arange(9, N, 10))

# Labels for major ticks
ax.set_xticklabels(np.arange(10, N+1, 10))
ax.set_yticklabels(np.arange(10, N+1, 10))

# Minor ticks
ax.set_xticks(np.arange(-.5, N, 1), minor=True)
ax.set_yticks(np.arange(-.5, N, 1), minor=True)

# Gridlines based on minor ticks
ax.grid(which='minor', color='k', linestyle='-', linewidth=0.5)
# ax.grid(which='major', color='g', linestyle='--', linewidth=2)

cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.tight_layout()
plt.show()
