#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
from skimage import data
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK: # double click event!
        cv2.circle(img,(x,y),100,(255,0,0),-1)
#     elif event == cv2.EVENT_FLAG_LBUTTON:
#         print("x :",x,"y :" ,y)
#         print("BGR : ",img[y,x,:])
    
def draw_rec(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK: # double click event!
        cv2.rectangle(img,(x,y),(x+100,y+100),(255,0,0),-1)
        
# Create a black image, a window and bind the function to window
astro = data.astronaut()
img = astro
img = data.astronaut()
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
mode = 0
while(1):    
    cv2.imshow('image',img)
    if cv2.waitKey(5) & 0xFF == 27: # enter ESC
        break
    elif cv2.waitKey(5)& 0xFF == 48:
        if(mode == 1):
            print("Mode = draw rec")
            cv2.setMouseCallback('image',draw_rec)
            mode = 0
        else:
            print("Mode = draw cir")
            cv2.setMouseCallback('image',draw_circle)
            mode = 1
cv2.destroyAllWindows()

