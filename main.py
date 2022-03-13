import cv2
from copy import copy,deepcopy
import helper as h
import diretion_gene as d
img = cv2.imread("hostim.jpg", 0)
sec_img=cv2.imread("secret2.png",0)
y_=deepcopy(img)
x_=deepcopy(sec_img)
pix=y_.tolist()
pix_secret=x_.tolist()
# converting decimal to binary
for i in range(len(pix_secret)):
    for j in range(len(pix_secret)):
        pix_secret[i][j]=bin(pix_secret[i][j]).replace("0b", "")
temp3=[]
temp3+=h.conversion_8bit(pix_secret)
print(d.return_psnr(pix,temp3))
# print(len(temp3))

