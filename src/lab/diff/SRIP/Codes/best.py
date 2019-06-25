# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 18:12:10 2019

@author: Akhil
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 00:42:06 2019

@author: Akhil
"""

import numpy as np
import cv2
from PIL import Image


img= cv2.imread('Bliz.BMPW_',0)
ret,gray=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#cv2.imshow('Orginal image',img);
cv2.imshow('Binary Image',gray);
print(gray);
cv2.waitKey(0)
cv2.destroyAllWindows()


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
    #print(m)
    for k in range(1,m):
        for i in range(1,r):
            for j in range(1,c):
                 if(x[i,j]==0):
                    x[i,j] = 0;
                 else:
                    v1 = min(x[i-1, j-1],x[i, j-1],x[i-1, j]);
                    v2 = min(x[i-1, j+1],x[i+1, j],x[i+1, j+1]);
                    v= min(v1,v2);
                    if (x[i, j] >= v):
                        y[i,j]= v+1;
        x=y;
    print("working")
    return y
        
print(Distance_Transform(gray));

i= Image.fromarray(Distance_Transform(gray));
i.save('final.BMP');


#img = Image.open('BW_liz.BMP').convert('L')
#img_inverted = ImageOps.invert(img)
#np_img = np.array(img_inverted)
#np_img[np_img > 0] = 1
#print(np_img)
#f=open("mat1.txt","b+");
#f.w
#f.close();
#print(img);
#img.show();