# coding: utf-8
import tensorflow as tf
import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import cv2
import imutils
import numpy as np
import time
from os import system
from googletrans import Translator
import boto3
from playsound import playsound


background = None

def running_avg(image, aWeight):
    global background          #initialize background
    if background is None:
        background = image.copy().astype("float")
        return
    cv2.accumulateWeighted(image, background, aWeight)  #compute weighted average, accumulate it and update the background

def segment(image, threshold=25):
    global background
    diff = cv2.absdiff(background.astype("uint8"), image)      #find the absolute difference between background and current frame
    th = cv2.threshold(diff,threshold,255,cv2.THRESH_BINARY)[1]  #threshold the diff image so that we get the foreground
    (_, cnts, _) = cv2.findContours(th.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)   #get the contours in the thresholded image
    
    if len(cnts) == 0:       #return None, if no contours detected
        return
    else:
        segmented = max(cnts, key=cv2.contourArea)     #based on contour area, get the maximum contour which is the hand
        return (th, segmented)



if __name__ == "__main__":
    
    aWeight = 0.5
    camera = cv2.VideoCapture(0)
    top, right, bottom, left = 2, 200, 350, 450    #ROI coordinates
    num_frames = 0
    
    
    while(True):
        (grabbed, frame) = camera.read()    #current frame
        frame = imutils.resize(frame, width=700)
        frame = cv2.flip(frame, 1)     #flip frame
        clone = frame.copy()
        (height, width) = frame.shape[:2]
        roi = frame[top:bottom, right:left]
        
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)    #convert ROI to grayscale
        gray = cv2.GaussianBlur(gray, (7, 7), 0)        #Blur ROI
        
    
        if num_frames < 10:      #to get the background, keep looking till a threshold is reached, so that our running average model gets calibrated
                running_avg(gray, aWeight)
        else:
            hand = segment(gray)                 # segment the hand region
            if hand is not None:
                (th, segmented) = hand
                
                cv2.drawContours(clone, [segmented + (right, top)], -1, (0, 0, 255))
                cv2.imshow("Thesholded", th)
                
                count = 1
                while(count>0):
                    time.sleep(0.01)
                    cv2.imwrite("test%d"%count+".jpg",th)
                    
                    #Classification of image using trained model
                    image_path = "test%d.jpg"%count
                    image_data = tf.gfile.FastGFile(image_path, 'rb').read()
                    label_lines = [line.rstrip() for line in tf.gfile.GFile("tf_files/retrained_labels.txt")]

                    with tf.gfile.FastGFile("tf_files/retrained_graph.pb", 'rb') as f:
                        graph_def = tf.GraphDef()
                        graph_def.ParseFromString(f.read())
                        _ = tf.import_graph_def(graph_def, name='')

                    with tf.Session() as sess:
                        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
                        predictions = sess.run(softmax_tensor,{'DecodeJpeg/contents:0': image_data})
                        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
                        for node_id in top_k:
                            human_string = label_lines[node_id]
                            score = predictions[0][node_id]
                            if score>0.3:
                                print('%s ' %human_string)
                                #system('say %s'%human_string)
                                
                                #Translation the label to Other Language: Hindi
                                translator = Translator()
                                ab = translator.translate('%s'%human_string, dest='hi')
                                abc = ab.text
                                print('%s'%abc)
                                
                                #Using Amazon Polly for tts service
                                polly_client = boto3.Session(aws_access_key_id='AKIAJPDR33VD2SK5SIAQ', aws_secret_access_key='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', region_name='us-west-2').client('polly')
                            
                                response = polly_client.synthesize_speech(VoiceId='Aditi', OutputFormat='mp3', Text = abc)
                                
                                file = open('speech.mp3', 'wb')
                                file.write(response['AudioStream'].read())
                                file.close()
                                playsound('/Users/juliaannjose/Documents/MinorProject/example_code/Custom-Image-Classification-using-Inception-v3/speech.mp3')
                            break
                    count= count -1

        
        #Segmented Hand Frame
        cv2.rectangle(clone, (left, top), (right, bottom), (0,255,0), 2)
        num_frames += 1
        cv2.imshow("Video Feed", clone)


        keypress = cv2.waitKey(1) & 0xFF
        if keypress == ord("q"):
            break

camera.release()
cv2.destroyAllWindows()

