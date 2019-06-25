import cv2
def main():
     img= cv2.imread(r"C:\Users\Akhil\srip\image-processing-iiith\src\lab\images\www.jpg",0)
     ret,gray=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
     #cv2.imshow('Orginal image',img);
     cv2.imshow('Binary Image',gray);
     print(gray);
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     
if __name__ =="__main__":
       main()