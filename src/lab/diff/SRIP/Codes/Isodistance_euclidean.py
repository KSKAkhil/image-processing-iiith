# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 19:38:33 2019

@author: Akhil
"""
import numpy as np
def Isodistance_eucledian(x1,y1,dist):
    a= np.zeros((16, 16))
    print(a)
    for i in range(0,16):
       for j in range(0,16):
         if (((x1-i)**2)+((y1-j)**2) == int((dist)**2)):
             a[i,j] = 1;
    print("Iso Distance plot is:")
    print(a)
    for i in range(0,16):
       for j in range(0,16):
           if (a[i,j]==1):
               print(i,j);
               
#Isodistance_eucledian(7,7,2.23606797749979)
             
           
           
    
