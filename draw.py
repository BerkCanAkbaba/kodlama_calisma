# import cv2 as cv
# import numpy as np

# blank = np.zeros((500,500,3),dtype="uint8")
# cv.imshow("Blank",blank)

# 1. Paint the image a certain colour

# blank[200:300, 300:400]=  0,0,255
# cv.imshow("Red",blank)

# 2. Draw a Rectangle

# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//1),(255,0,0),thickness=-1)
# cv.imshow("Blue Rectangle",blank)

# 3. Draw a Circle

# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(255,0,0),thickness=-1)
# cv.imshow("Blue Circle",blank)

# 4. Draw a line

# cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=3)
# cv.imshow("Blue Line",blank)

#5. Write text

# cv.putText(blank,"Hello my name is Berk Can",(0,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,0,0),thickness=2)
# cv.imshow("Blue Text",blank)

# cv.waitKey(0)