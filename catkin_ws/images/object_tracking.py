import cv2
import numpy as np
img=cv2.imread('camera001.jpeg')
c=1
while img.any()!=None:
    print "Received"
    x=img.shape[0]
    y=img.shape[1]
    for i in range (x):
    	for j in range (y):
    		if img.item(i,j,2)>img.item(i,j,1) and img.item(i,j,2)>img.item(i,j,0):
    			img.itemset((i,j,0),0)
    			img.itemset((i,j,1),0)
    		else:
    			img.itemset((i,j,0),0)
    			img.itemset((i,j,1),0)
    			img.itemset((i,j,2),0)
    if c<10:
        c ='00'+str(c)
    elif c<100:
        c ='0'+str(c)
    elif c<1000:
        c = str(c)
    name='obimages/modify'+c+'.jpeg'
    name2='camera'+c+'.jpeg'
    cv2.imwrite(name,img)
    c=int(c)+1
    img=cv2.imread(name2)
