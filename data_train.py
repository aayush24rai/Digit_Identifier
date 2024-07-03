#Data Preparation, Training and Evaluation
import cv2
import numpy as np

#Input the digits dataset
image = cv2.imread('/home/aayushrai/Projects/Handwritten Digit Identifier/Handwritten_Digit_Identifier/digits.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
small = cv2.pyrDown(image)

cv2.imshow('Digits Dataset', small)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Split the image to 5000 cells, each 20x20px
#SO we get a 4D array => 50 x 100 x 20 x 20px
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]


#Covert this 'List' we made into Numpy Array (50, 100, 20, 20)
x = np.array(cells)
print("The shape of our cells array: " + str(x.shape))

#Splitting the data set into 2 fragements 
#70% => training, 30% => testing
train = x[:,:70].reshape(-1,400).astype(np.float32)
test = x[:,70:100].reshape(-1,400).astype(np.float32)

#Data Labelling
k = [0,1,2,3,4,5,6,7,8,9]
train_labels = np.repeat(k,350)[:,np.newaxis]
test_labels = np.repeat(k,150)[:,np.newaxis]

#Inititiate K-Nearest Neighbors
knn = cv2.ml.KNearest_create()
#Train the data
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
#Test the trained model with data for k=3
ret, result, neighbors, distance = knn.findNearest(test, k=3)

#Checking the accuracy of classification
#by comparing the result with test_labels
#and checking the wrong matches
matches = result = test_labels
correct = np.count_nonzero(matches)
accuracy = correct * (100.0/result.size)

print("Accuracy is = %.2f" % accuracy + "%")