import cv2
import numpy as np

# mouse callback function
def pick_color(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = image[y,x]
        #you might want to adjust the ranges(+-10, etc):
        upper =  np.array([pixel[0] + 10, pixel[1] + 10, pixel[2] + 10])
        lower =  np.array([pixel[0] - 10, pixel[1] - 10, pixel[2] - 10])
        print(pixel, lower, upper)
        image_mask = cv2.inRange(image,lower,upper)
        cv2.imshow("mask",image_mask)
image = cv2.imread(r'D:/Python_code/opencv/1.jpg')
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', pick_color)
cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()