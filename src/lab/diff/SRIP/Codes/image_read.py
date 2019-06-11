import cv2
def main():
     img= cv2.imread(r"C:\\Users\\Akhil\\srip\\image-processing-iiith\\src\\lab\\diff\\boom.png",0)
     print(img)
     cv2.imshow('image',img)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     
if __name__ =="__main__":
       main()