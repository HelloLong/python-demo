# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 18:05:06 2019

@author: lh_xu
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.random.seed(2000)
y = np.random.standard_normal((1000, 2))
plt.figure(figsize=(7,5))
plt.hist(y,label=['1st','2nd'],bins=25)
plt.grid(True)
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('Histogram')
plt.show()