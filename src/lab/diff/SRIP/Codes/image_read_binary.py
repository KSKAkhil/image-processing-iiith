import cv2
def main():
     img= cv2.imread(r"C:\Users\Akhil\srip\image-processing-iiith\src\lab\images\BW_liz.BMP")
     print(img)
     cv2.imshow('image',img)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     
if __name__ =="__main__":
       main()