# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:55:10 2019

@author: lh_xu
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.random.seed(1000)
y = np.random.standard_normal(10)
print ("y = %s" % y)
x = range(len(y))
print ("x=%s" % x)
plt.plot(y)
plt.show()