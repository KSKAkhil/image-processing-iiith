# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:33:35 2019

@author: Akhil
"""

def Chess_Board(x1,y1,x2,y2):
    dist=0.0;
    m1=abs(x1-x2);
    m2=abs(y1-y2);
    if(m1>m2):
        dist=m1;
    else:
        dist=m2
    return dist;
#example
print(Chess_Board(0,0,15,15))