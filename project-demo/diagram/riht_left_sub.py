# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 18:02:23 2019

@author: lh_xu
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.random.seed(2000)
y = np.random.standard_normal((10, 2))

plt.figure(figsize=(10,5))
plt.subplot(121)  #两行一列,第一个图
plt.plot(y[:,0], lw = 1.5,label = '1st')
plt.plot(y[:,0], 'ro')
plt.grid(True)
plt.legend(loc = 0) #图例位置自动
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('1st Data Set')

plt.subplot(122)
plt.bar(np.arange(len(y)), y[:,1],width=0.5, color='g',label = '2nc')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.xlabel('index')
plt.title('2nd Data Set')
plt.show()