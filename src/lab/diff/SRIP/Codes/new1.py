# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 00:42:06 2019

@author: Akhil
"""

from PIL import Image, ImageOps
import numpy as np
img = Image.open('BW_liz.BMP').convert('L')
img_inverted = ImageOps.invert(img)
np_img = np.array(img_inverted)
np_img[np_img > 0] = 1
print(np_img)
#f=open("mat1.txt","b+");
#f.w
#f.close();
print(img);
img.show();

def Distance_Transform(y):
    r = len(y)
    c = len(list(zip(*y)))
    #return np.shape(x)//
    x= np.zeros((r, c));
    #print(x);
    #print(r);
    #print(c)
    m = max(r,c);
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
                    y[i,j]= v+1;
        x=y;
    return y
        
print(Distance_Transform(np_img));

i= Image.fromarray(Distance_Transform(np_img));
i.save('new2.BMP');