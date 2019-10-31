# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import mathtool
import matplotlib.pyplot as plt
def dy(y):
    return -y
xs=[0,1,2,3,4,5]
ys=mathtool.euler(dy,0,10,xs)
plt.plot(xs,ys)