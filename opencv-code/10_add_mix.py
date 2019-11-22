#encoding:utf-8
from cv2 import cv2  
import numpy as np  
from matplotlib import pyplot as plt
import random
import copy
 
#读取图片
img1 = cv2.imread('test3.jpg')
img2 = cv2.imread('test4.jpg')
# (h1,w1)=np.shape(img1)[:2]
# (h2,w2)=np.shape(img2)[:2]
# img1 = cv2.resize(img1, (int(w/3),int(h/3)), interpolation=cv2.INTER_CUBIC)


#cv2.imshow("o",img)
source = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
noise = cv2.cvtColor(n,cv2.COLOR_BGR2RGB)
result = cv2.cvtColor(r,cv2.COLOR_BGR2RGB)

#显示图形
titles = ['Source Image', 'Noise Image', 'Blur Image']  
images = [source, noise, result]  
for i in range(3):  
   plt.subplot(1,3,i+1), plt.imshow(images[i], 'gray')  
   plt.title(titles[i])  
   plt.xticks([]),plt.yticks([])  
plt.show()  