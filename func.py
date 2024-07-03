#Defining all functions we will use to prepare an input image
import numpy as np
import cv2

#Takes a contour and outputs the x centroid coordinates
def x_centroid(contour):
    #if cv2.contourArea(contour) > 10:
        M = cv2.moments(contour)
        return (int(M['m10']/M['m00']))


#Takes an image and mkaes the dimensions square
#by adding black pixels as per need
def makeSquare(img):
    BLACK = [0,0,0]

    img_dim = img.shape
    height = img_dim[0]
    width = img_dim[1]

    if height == width:
        square = img
        return square

    else:
        doublesize = cv2.resize(img, (2*width, 2*height), interpolation = cv2.INTER_CUBIC)
        height *= 2
        width *= 2

        if height > width :
            pad = int((height - width)/2)
            doublesize_square = cv2.copyMakeBorder(doublesize, 0, 0, pad, pad, cv2.BORDER_CONSTANT, value=BLACK)
        else:
            pad = (width - height)/2
            doublesize_square = cv2.copyMakeBorder(doublesize, pad, pad, 0,
                                                   0, cv2.BORDER_CONSTANT, value=BLACK)
    
    doublesize_square_dim = doublesize_square.shape
    return doublesize_square


#Function to re-size the image to specified dimensions
def resize_to_pixel(dimensions, image):
    buffer_px = 4
    dimensions = dimensions - buffer_px
    squared = image

    r = float(dimensions) / squared.shape[1]
    dim = (dimensions, int(squared.shape[0] * r))
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    img_dim2 = resized.shape
    height_r = img_dim2[0]
    width_r = img_dim2[1]
    BLACK = [0,0,0]

    if height_r > width_r:
        resized = cv2.copyMakeBorder(resized,0,0,0,1,cv2.BORDER_CONSTANT, value=BLACK)
    if height_r < width_r:
        resized = cv2.copyMakeBorder(resized,1,0,0,0,cv2.BORDER_CONSTANT, value=BLACK)
    
    p = 2
    ReSizedImg = cv2.copyMakeBorder(resized,p,p,p,p,cv2.BORDER_CONSTANT, value=BLACK)
    img_dim = ReSizedImg.shape
    
    return ReSizedImg