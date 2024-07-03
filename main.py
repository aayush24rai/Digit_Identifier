import cv2
import numpy as np

from func import *
from data_train import *

image = cv2.imread('/home/aayushrai/Projects/Handwritten Digit Identifier/Handwritten_Digit_Identifier/numbers.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("image", image)
cv2.imshow("gray", gray)
cv2.waitKey(0)

#Blur the image and find canny edges
blurred = cv2.GaussianBlur(gray, (5,5), 0)
cv2.imshow("blurred", blurred)
cv2.waitKey(0)

edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("edged", edged)
cv2.waitKey(0)


#Find contours
contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Sort out contours left to right by using x coordinates
contours = sorted(contours, key=x_centroid, reverse=False)

#Create empty array to store entire number
full_number = []

#loop over the contours
for c in contours:
    #computing the bounding box 
    (x,y,w,h) = cv2.boundingRect(c)

    if w >= 5 and h >= 25:
        roi = blurred[y:y+h, x:x+w]
        ret, roi = cv2.threshold(roi, 127, 255, cv2.THRESH_BINARY_INV)
        squared = makeSquare(roi)
        final = resize_to_pixel(20, squared)
        cv2.imshow("final", final)

        final_array  = final.reshape((1, 400))
        final_array = final_array.astype(np.float32)
        ret, result, neighbours, dist = knn.findNearest(final_array, k=1)
        
        number = str(int(float(result[0])))
        full_number.append(number)

        cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 2)
        cv2.putText(image, number, (x, y + 155), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0), 2)
        cv2.imshow("image", image)
        cv2.waitKey(0)

cv2.destroyAllWindows()
print("The number is: " + ''.join(full_number))