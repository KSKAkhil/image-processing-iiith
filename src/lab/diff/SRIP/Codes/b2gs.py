# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:35:41 2019

@author: Akhil
"""
import random
import numpy as np
def Distance_Transform(x):
    print(x);
    
    
    
    
    
    
    
    
    
    
    
    
#edge dect.
a= np.zeros((16, 16));
    #a= np.array([random.sample(range(16),c) for x in range(r)]);
    #print(a);
for i in range(0,16):
    for j in range(0,16):
          a[i,j] = random.randrange(0, 2);
   
Distance_Transform(a);