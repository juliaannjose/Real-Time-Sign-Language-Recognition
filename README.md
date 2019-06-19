# Real-Time-Sign-Language-Recognition
Image-based approach to Sign Language Recognition.

## Introduction
Sign Language is the form of communication among deaf & dumb people. They use signs and gestures to convey messages and express themselves to others. This would require both the parties involved in the communication process to know the meaning of the signs/gestures that the other person is trying to convey. Since we cannot expect everyone to know the meaning of different signs/gestures, this system acts as a medium that converts signs/gestures to speech.

Sign Language Recognition is a challenage that can be approached in many ways. Two of its main approaches are sensor-based and image-based. This system uses the image-based approach to sign language recognition.

##Methodology
In this approach, with the help of a camera, dynamic images are send as input to the image-based system. The video sequence, which is a series of frames of images, is then analyzed. Google’s Inception v3 model is then used for image classification purpose of these sign gestures.
The dataset needed in this approach will require you to take images in different backgrounds, varied lighting conditions, etc. Consequently, this will introduce a number of problems such as segmentation of hand from the background, etc. To overcome this problem and to ease this challenge, the dataset can be modified.
The modified dataset will basically be background subtracted and binary thresholded images of the gestures. The dataset will now look like this:
