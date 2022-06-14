#Autocar traitement image contour
import numpy as np
import cv2
import time
import random
import collections
import os
import urllib.request


class AC_Imagecontour(object):
    def __init__(self):
        print(' ----- AutoCar : Starting Traitement part.')


    def run(self, img_arr):
            if img_arr is None:
                return img_arr

            img_arrori=img_arr.copy()
            #img_arr = cv2.cvtColor(img_arr,cv2.COLOR_BayerGR2RGB)
            img_arr = cv2.cvtColor(img_arr, cv2.COLOR_BGRA2GRAY)
            img_arr[np.where(img_arr <= 180)] = 0
            #img_arr = cv2.Canny(img_arr, 20, 65,7)
            img_arr = cv2.Canny(img_arr, 35, 40, L2gradient = True)
            #img_arr = cv2.Canny(img_arr, 30, 60,3)
            pt1 = (0, 60)
            pt2 = (0, 0)
            pt3 = (100, 0)
            pt4 = (160, 60)
            pt5 = (160, 0)
            pt6 = (60, 0)

            triangle_cnt = np.array( [pt1, pt2, pt3] )
            triangle_cnt2 = np.array( [pt4, pt5, pt6] )

            cv2.drawContours(img_arr, [triangle_cnt], 0, (0,255,0), -1)
            cv2.drawContours(img_arr, [triangle_cnt2], 0, (0,255,0), -1)
            cv2.rectangle(img_arr, (0, 0), (160, 40), (0, 0, 0), -1)
            #cv2.imwrite('imagemodified.png',img_arr)

            return img_arr, img_arrori
