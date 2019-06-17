import cv2
from skimage.exposure import rescale_intensity
from skimage.segmentation import slic
from skimage.util import img_as_float
from skimage import io
import numpy as np


Folder="training_dataset/Hello"
Ext=".jpg"


def resize_image(image,w,h):
    image=cv2.resize(image,(w,h))
    cv2.imwrite(Folder+"/Resize-"+str(w)+"*"+str(h)+ image_file + Ext, image)

def padding_image(image,topBorder,bottomBorder,leftBorder,rightBorder,color_of_border=[0,0,0]):
    image = cv2.copyMakeBorder(image,topBorder,bottomBorder,leftBorder,
        rightBorder,cv2.BORDER_CONSTANT,value=color_of_border)
    cv2.imwrite(Folder+ "/padd-" + str(topBorder) + str(bottomBorder) + "*" + str(leftBorder) + str(rightBorder) + image_file +  Ext, image)

def flip_image(image,dir):
    image = cv2.flip(image, dir)
    cv2.imwrite(Folder + "/flip-" + str(dir)+ image_file + Ext, image)

def invert_image(image,channel):
    image=(channel-image)
    cv2.imwrite(Folder + "/invert-"+str(channel)+ image_file + Ext, image)

def add_light(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    image=cv2.LUT(image, table)
    if gamma>=1:
        cv2.imwrite(Folder + "/light-"+str(gamma)+ image_file + Ext, image)
    else:
        cv2.imwrite(Folder + "/dark-" + str(gamma) + image_file +  Ext, image)

def add_light_color(image, color, gamma=1.0):
    invGamma = 1.0 / gamma
    image = (color - image)
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    image=cv2.LUT(image, table)
    if gamma>=1:
        cv2.imwrite(Folder+ "/light_color-"+str(gamma)+ image_file + Ext, image)
    else:
        cv2.imwrite(Folder + "/dark_color" + str(gamma) + image_file +  Ext, image)

def saturation_image(image,saturation):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    v = image[:, :, 2]
    v = np.where(v <= 255 - saturation, v + saturation, 255)
    image[:, :, 2] = v

    image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    cv2.imwrite(Folder + "/saturation-" + str(saturation)  + image_file + Ext, image)

def multiply_image(image,R,G,B):
    image=image*[R,G,B]
    cv2.imwrite(Folder+"/Multiply-"+str(R)+"*"+str(G)+"*"+str(B)+Ext, image)

def averageing_blur(image,shift):
    image=cv2.blur(image,(shift,shift))
    cv2.imwrite(Folder + "/AverageingBLur-" + str(shift) + Ext, image)

def sharpen_image(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    image = cv2.filter2D(image, -1, kernel)
    cv2.imwrite(Folder+"/Sharpen-"+Ext, image)

def grayscale_image(image):
    image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(Folder + "/Grayscale-" + Ext, image)

def median_blur(image,shift):
    image=cv2.medianBlur(image,shift)
    cv2.imwrite(Folder + "/MedianBLur-" + str(shift) + Ext, image)

def bileteralBlur(image,d,color,space):
    image = cv2.bilateralFilter(image, d,color,space)
    cv2.imwrite(Folder + "/BileteralBlur-"+str(d)+"*"+str(color)+"*"+str(space)+ Ext, image)

def erosion_image(image,shift):
    kernel = np.ones((shift,shift),np.uint8)
    image = cv2.erode(image,kernel,iterations = 1)
    cv2.imwrite(Folder + "/Erosion-"+"*"+str(shift) + Ext, image)

def dilation_image(image,shift):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.dilate(image,kernel,iterations = 1)
    cv2.imwrite(Folder + "/Dilation-" + "*" + str(shift)+ Ext, image)

def morphological_gradient_image(image, shift):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    cv2.imwrite(Folder + "/Morphological_Gradient-" + "*" + str(shift) + Ext, image)

def top_hat_image(image, shift):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
    cv2.imwrite(Folder + "/Top_Hat-" + "*" + str(shift) + Ext, image)

def black_hat_image(image, shift):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
    cv2.imwrite(Folder + "/Black_Hat-" + "*" + str(shift) + Ext, image)


image_file = "test0.jpg"
image=cv2.imread(Folder + "/" + image_file)


padding_image(image,100,0,0,0)#(y1,y2,x1,x2)
padding_image(image,0,100,0,0)
padding_image(image,0,0,100,0)
padding_image(image,0,0,0,100)
padding_image(image,100,100,100,100)

flip_image(image,0)#horizontal
flip_image(image,1)#vertical
flip_image(image,-1)#both

invert_image(image,255)
invert_image(image,100)

add_light(image,1.5)
add_light(image,2.0)
add_light(image,2.5)
add_light(image,3.0)
add_light(image,4.0)
add_light(image,5.0)
add_light(image,0.7)
add_light(image,0.4)
add_light(image,0.3)
add_light(image,0.1)

add_light_color(image,255,1.5)
add_light_color(image,255,0.7)

saturation_image(image,50)
saturation_image(image,100)
saturation_image(image,150)
saturation_image(image,200)

multiply_image(image,0.5,1,1)
multiply_image(image,1,0.5,1)
multiply_image(image,1,1,0.5)
multiply_image(image,0.5,0.5,0.5)

averageing_blur(image,5)
averageing_blur(image,4)
averageing_blur(image,6)

sharpen_image(image)
grayscale_image(image)

median_blur(image,3)
median_blur(image,5)
median_blur(image,7)

bileteralBlur(image,9,75,75)
bileteralBlur(image,12,100,100)
bileteralBlur(image,25,100,100)
bileteralBlur(image,40,75,75)

erosion_image(image,1)
erosion_image(image,3)
erosion_image(image,6)

dilation_image(image,1)
dilation_image(image,3)
dilation_image(image,5)

morphological_gradient_image(image,5)
morphological_gradient_image(image,10)
morphological_gradient_image(image,15)

top_hat_image(image,200)
top_hat_image(image,300)
top_hat_image(image,500)

black_hat_image(image,200)
black_hat_image(image,300)
black_hat_image(image,500)
