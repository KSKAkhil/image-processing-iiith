# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:35:41 2019

@author: Akhil
"""
import random
import numpy as np
#edge dect.
a= np.zeros((16, 16));
    #a= np.array([random.sample(range(16),c) for x in range(r)]);
    #print(a);
for i in range(0,16):
    for j in range(0,16):
         a[i,j] = random.randrange(1, 2);
         
def Distance_Transform(x):
    r = len(x)
    c = len(list(zip(*x)))
    #return np.shape(x)
    print(x);
    print(r);
    print(c)
    for i in range(0,16):
        for j in range(0,16):
            v1 = min(x[i-1, j-1],x[i, j-1],x[i-1, j]);
            v2 = min(x[i-1, j+1],x[i+1, j],x[i+1, j+1]);
            print(v1);
            print(v2);
            print("ok")
            #x[i,j]= v+1;
    #return     

         
         
Distance_Transform(a);