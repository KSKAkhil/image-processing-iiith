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
         a[i,j] = random.randrange(2, 3);
         #a[7,7]=1;
         #a[3,3]=1;
print(a)
def Distance_Transform(y):
    r = len(y)
    c = len(list(zip(*y)))
    #return np.shape(x)
    x= np.zeros((r, c));
    #print(x);
    #print(r);
    #print(c)
    m = max(r,c)
    x=y;
    for k in range(1,m):
        for i in range(1,15):
            for j in range(1,15):
                if(x[i,j]==0):
                    x[i,j] = 0;
                else:
                    v1 = min(x[i-1, j-1],x[i, j-1],x[i-1, j]);
                    v2 = min(x[i-1, j+1],x[i+1, j],x[i+1, j+1]);
                    v= min(v1,v2);
                    if (x[i, j] >= v):
                        y[i,j]= v+1;
        x=y;
    return y;
         

         
         
print(Distance_Transform(a));