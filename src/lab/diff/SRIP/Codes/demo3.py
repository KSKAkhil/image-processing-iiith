# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 23:28:41 2019

@author: Akhil
"""

import cv2
import numpy as np
def main():
    img = cv2.imread(r"C:\Users\Akhil\srip\image-processing-iiith\src\lab\images\BW_liz.BMP",0)
    ret,thresh_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    print(img)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows();
if __name__ =="__main__":
       main()
     