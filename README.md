# Real-Time-Sign-Language-Recognition
Image-based approach to Sign Language Recognition.

## Introduction
Sign Language is the form of communication among deaf & dumb people. They use signs and gestures to convey messages and express themselves to others. This would require both the parties involved in the communication process to know the meaning of the signs/gestures that the other person is trying to convey. Since we cannot expect everyone to know the meaning of different signs/gestures, this system acts as a medium that converts signs/gestures to speech.

Sign Language Recognition is a challenage that can be approached in many ways. Two of its main approaches are sensor-based and image-based. This system uses the image-based approach to sign language recognition.

## Methodology
In this approach, with the help of a camera, dynamic images are send as input to the image-based system. The video sequence, which is a series of frames of images, is then analyzed. Google’s Inception v3 model is then used for image classification purpose of these sign gestures.

The dataset needed in this approach will require you to take images in different backgrounds, varied lighting conditions, etc. Consequently, this will introduce a number of problems such as segmentation of hand from the background, etc. To overcome this problem and to ease this challenge, the dataset can be modified.
The modified dataset will basically be background subtracted and binary thresholded images of the gestures. The dataset will now look like this:

![alt text](https://github.com/juliajose97/Real-Time-Sign-Language-Recognition/blob/master/training_dataset/Language/padd-1000*00test27.jpg.jpg)
![alt text](https://github.com/juliajose97/Real-Time-Sign-Language-Recognition/blob/master/training_dataset/Fine/padd-1000*00test10.jpg.jpg)
![alt text](https://github.com/juliajose97/Real-Time-Sign-Language-Recognition/blob/master/training_dataset/Sign/padd-1000*00test29.jpg.jpg)

The training dataset thus obtained is used with Google's Inception v3 model for image classification. 

## Usage Instructions
### 1. Creating the dataset
    $ python 
This will detect the foreground (hand, in this case) and apply binary thresholding to your images.

    $ python Data_Augmentation.py
This will flip, rotate, resize, invert, etc your images. (I manually captured 31 images for a single sign and used this to get 800+ images from them)
### 2. Training an image classifier with [Google's Inception v3](https://www.tensorflow.org/hub/tutorials/image_retraining)  
    $ python train_data.py
### 3. Real-Time Recognition
    $ python Sign_Language_Recognition.py
This program will do real-time processing of images from the camera, applying binary thresholding simultaneously and test these images using the classifier obtained above. 
### 4. Sign to Speech
Upon detection & recognition of the gestures, the given texts (labels) are converted to speech. Additionally, the text is translated to Hindi (from English) and with the help of Amazon polly, the text in Hindi is converted to speech. 
    
## References
