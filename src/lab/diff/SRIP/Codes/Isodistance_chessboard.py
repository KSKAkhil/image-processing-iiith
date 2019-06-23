# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 22:27:04 2019

@author: Akhil
"""

import numpy as np
def Isodistance_chessboard(x1,y1,dist):
    a= np.zeros((16, 16))
    print(a)
    for i in range(0,16):
       for j in range(0,16):
         m1=abs(x1-i);
         m2=abs(y1-j);
         if (dist==m1):
                 if(m1>=m2):
                     a[i,j] = 1;
         elif (dist==m2):
               if(m2>=m1):
                     a[i,j] = 1;
         else:
            print("");
    print("Iso Distance plot is:")
    print(a)
    for i in range(0,16):
       for j in range(0,16):
           if (a[i,j]==1):
               print(i,j);
#Isodistance_chessboard(4,4,3)