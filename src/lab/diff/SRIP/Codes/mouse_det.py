import numpy as np 
import cv2
class LoadImage:
    def loadImage(self):
            self.img=cv2.imread(r"C:\\Users\\Akhil\\srip\\image-processing-iiith\\src\\lab\\diff\\overlay.png")
            cv2.imshow('Test',self.img)

            self.pressedkey=cv2.waitKey(0)

            # Wait for ESC key to exit
            if self.pressedkey==27:
                cv2.destroyAllWindows()

    # Start of the main program here        
    if __name__=="__main__":
        LI=LoadImage()
        LI.loadImage()