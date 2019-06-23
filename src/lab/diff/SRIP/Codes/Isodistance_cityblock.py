# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 23:07:33 2019

@author: Akhil
"""

import numpy as np
def Isodistance_cityblock(x1,y1,dist):
    a= np.zeros((16, 16))
    print(a)
    for i in range(0,16):
       for j in range(0,16):
         if((abs(x1-i)+abs(y1-j))== dist):
                 a[i,j] = 1;
    print("Iso Distance plot is:")
    print(a)
    for i in range(0,16):
       for j in range(0,16):
           if (a[i,j]==1):
               print(i,j);
               
#Isodistance_cityblock(7,7,2)
             