#Autocar course reader pour une course dans les regles
import numpy as np
import cv2
import time
import random
import collections
import os
import urllib.request
import sys

from PIL import Image

class AC_CourseManage(object):
    def __init__(self,nombredetours):
        print(' ----- AutoCar : Starting Yellow viewer part.')
        self._on = True
        self.Started=False
        self.Stopped=True

        self.nbrtours=nombredetours + 1
        self.tourseffectue=0
        self.awaitimages=0
        self.testpassage=False

    def update(self):
            time.sleep(1)

    def run(self, img_arr,angle, throttle):
        if img_arr is not None:
                #Verifie le nombre de tourseffectue
                if(self.tourseffectue<self.nbrtours):
                    #print(self.awaitimages)
                    if(self.awaitimages==0):
                        img_cp=img_arr.copy()
                        cv2.rectangle(img_cp, (0, 0), (160, 80), (0, 0, 0), -1)
                        cv2.rectangle(img_cp, (0, 0), (40, 120), (0, 0, 0), -1)
                        cv2.rectangle(img_cp, (120, 0), (160, 120), (0, 0, 0), -1)
                        YELLOW_MIN = np.array([80 , 80, 0], dtype="uint8")
                        YELLOW_MAX = np.array([255, 255, 0], dtype="uint8")
                        mask = cv2.inRange(img_cp, YELLOW_MIN, YELLOW_MAX)
                        output = cv2.bitwise_and(img_cp,img_cp,mask=mask)
                        summed=np.sum(output!=0)
                        #if(summed >1200):
                        print(summed)
                        if(summed >30):
                             print("Tour numéro:"+str(self.tourseffectue))
                             self.testpassage = True

                        if(self.testpassage):
                            self.testpassage = False
                            self.tourseffectue=self.tourseffectue+1
                            self.awaitimages=300
                    else:
                        self.awaitimages=self.awaitimages-1
                else:
                    print("Course fini")
                    angle=0.0
                    throttle=0.0
                    self.Stopped=False
                    self.Started=False

                if(self.Stopped):
                    img_cp=img_arr.copy()
                    img_cp=cv2.rectangle(img_cp, (0, 40), (160, 120), (0, 0, 0), -1)
                    img_cp=cv2.rectangle(img_cp, (0, 0), (40, 120), (0, 0, 0), -1)
                    img_cp=cv2.rectangle(img_cp, (120, 0), (160, 120), (0, 0, 0), -1)
                    lower = np.array([0, 150, 0], dtype="uint8")
                    upper = np.array([150, 255, 150], dtype="uint8")

                    mask = cv2.inRange(img_cp, lower, upper)
                    output = cv2.bitwise_and(img_cp, img_cp, mask = mask)
                    summed = np.sum(output != 0)
                    angle=0.0
                    throttle=0.0
                    print(summed)
                    if(summed > 70):
                      print(summed)
                      print("Starting la course")
                      self.Started=True
                      self.Stopped=False



        return angle, throttle
