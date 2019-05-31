# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 18:06:32 2019

@author: lh_xu
"""

from matplotlib.patches import Polygon
import numpy as np
import matplotlib.pyplot as plt

#1. 定义积分函数
def func(x):
    return 0.5 * np.exp(x)+1

#2.定义积分区间
a,b = 0.5, 1.5
x = np.linspace(0, 2 )
y = func(x)
#3.绘制函数图形
fig, ax = plt.subplots(figsize=(7,5))
plt.plot(x,y, 'b',linewidth=2)
plt.ylim(ymin=0)
#4.核心， 我们使用Polygon函数生成阴影部分，表示积分面积：
Ix = np.linspace(a,b)
Iy = func(Ix)
verts = [(a,0)] + list(zip(Ix, Iy))+[(b,0)]
poly = Polygon(verts,facecolor='0.7',edgecolor = '0.5')
ax.add_patch(poly)
#5.用plt.text和plt.figtext在图表上添加数学公式和一些坐标轴标签。
plt.text(0.5 *(a+b),1,r"$\int_a^b f(x)\mathrm{d}x$", horizontalalignment ='center',fontsize=20)
plt.figtext(0.9, 0.075,'$x$')
plt.figtext(0.075, 0.9, '$f(x)$')
#6. 分别设置x,y刻度标签的位置。
ax.set_xticks((a,b))
ax.set_xticklabels(('$a$','$b$'))
ax.set_yticks([func(a),func(b)])
ax.set_yticklabels(('$f(a)$','$f(b)$'))
plt.grid(True)