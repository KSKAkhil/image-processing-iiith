# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:37:21 2019

@author: Akhil
"""


def Eucledian(x1,y1,x2,y2):
    dist=0;
    dist= ((x1-x2)**2+(y1-y2)**2)**0.5
    return dist;
#example
#print(Eucledian(12,12,1,2))