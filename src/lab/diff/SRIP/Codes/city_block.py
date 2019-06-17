# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:07:59 2019

@author: Akhil
"""

def City_Block(x1,y1,x2,y2):
    dist=0.0;
    dist= abs(x1-x2)+abs(y1-y2);
    return dist;
#example
#print(City_Block(12,12,6,7))