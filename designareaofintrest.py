# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 19:35:17 2022

@author: HP
"""

import cv2
import pickle
width,height=150,190
try:
    with open("a","rb") as f:
        poslist=pickle.load(f)
except:        
    poslist=[]
def on(events,x,y,flags,params):
    if events==cv2.EVENT_LBUTTONDOWN:
        poslist.append((x,y))
    if events==cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(poslist):
            x1,y1=pos
            if x1<x<x1+width and y1<y<y1+height:
                poslist.pop(i)
    with open("a","wb") as f:
        pickle.dump(poslist,f)           
while True:
    img=cv2.imread("a.jpg")
    for pos in poslist:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)
    #img=cv2.imread("a.jpg")
    #cv2.rectangle(img,(150,160),(300,350),(255,0,255),2)
    cv2.imshow("image",img)
    cv2.setMouseCallback("image", on)    
    if cv2.waitKey(40) == 27:
        break