# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:36:40 2019

@author: Akhil
"""

def Eight_connectivity(x1,y1,x2,y2,i1,i2):
    if(i1==i2):
        if(x1-1==x2 or x2==x1+1):
                 #print("wo1rkingxx");
                 if(y1==y2):
                    return 0;
                    #print("workingxx");
                 else:
                    return 1;
                    #print("not workingxx");
        if(y1-1==y2 or y2==y1+1):
                if(x1==x2):
                      return 0;
                      #print("working");
                else:
                    return 1;
        else:
            return 0;
                   # print("not working");
    else:
        return 0;
        #print("not working");
      # return 1 says they are 4 connected 
      # return 0 says they are not 4 connected
#print(Eight_connectivity(21,8,22,9,1,0)); 
