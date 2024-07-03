<h1 align="center" id="title">Handwritten Digit Recognition System</h1>

 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) 


<p align="center"><img src="https://socialify.git.ci/aayush24rai/Handwritten_Digit_Identifier/image?description=1&amp;descriptionEditable=Handwritten%20Digit%20Recognition%20System&amp;font=Inter&amp;language=1&amp;name=1&amp;owner=1&amp;pattern=Diagonal%20Stripes&amp;theme=Dark" alt="project-image"></p>

<p id="description">This project implements a system to recognize handwritten digits from images using OpenCV and Python. It utilizes the K-Nearest Neighbors (KNN) algorithm for machine learning with automated manual preparation and labeling of the training dataset derived from a single image of digits. The application is capable of preprocessing images extracting features and classifying digits providing a foundational approach for further exploration into optical character recognition (OCR).</p>

<h2>Computer Vision Pipeline Screenshots:</h2>

<img src="https://github.com/aayush24rai/Handwritten_Digit_Identifier/blob/main/Output/img_gray.png" alt="img_gray" width="878" height="613">
<img src="https://github.com/aayush24rai/Handwritten_Digit_Identifier/blob/main/Output/img_blur.png" alt="img_blurred" width="878" height="613">
<img src="https://github.com/aayush24rai/Handwritten_Digit_Identifier/blob/main/Output/img_edged.png" alt="img_edged" width="878" height="613">
<img src="https://github.com/aayush24rai/Handwritten_Digit_Identifier/blob/main/Output/final_output.png" alt="final_output" width="878" height="613">

  
  
<h2>✨ Features</h2>

Here're some of the project's best features:

*   _Custom Dataset Preparation:_ Extracts and labels data from a grid of handwritten digits.
*   _Digit Recognition:_ Identifies digits from 0 to 9 in images using the trained KNN model.
*   _Image Preprocessing:_ Includes grayscale conversion noise reduction edge detection and contour sorting.
*   _Accuracy Evaluation:_ Computes the accuracy of the model based on test data.
*   _Visualization:_ Displays images during various stages of preprocessing and recognition to help in debugging and understanding the process.

  
  
<h2>💻 Built with</h2>

Technologies used in the project:


*   Python: Primary programming language.
*   OpenCV: Utilized for image processing and implementation of the KNN algorithm.
*   NumPy: Manages data in arrays for efficient computation and handling.


<h2>🛠️ How it works</h2>

The system is structured into three main components:

* `data_train.py`: Manages the loading of a digit image, splits it into individual digit cells, labels them, and divides them into training and testing sets. This script also trains the KNN model using the prepared data.
* `func.py`: Provides utility functions for image manipulation such as making images square, resizing, and calculating centroid coordinates for sorting contours.
* `main.py`: Serves as the entry point of the program, processing new images for digit recognition using the trained model and utility functions.
