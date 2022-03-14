import cv2
from copy import copy,deepcopy
import helper as h
import diretion_gene as d

# getting host image
img = cv2.imread("hostim.jpg", 0)

# getting secret image
sec_img=cv2.imread("secret2.png",0)
y_=deepcopy(img)
x_=deepcopy(sec_img)

# converting to pixels
pix=y_.tolist()
pix_secret=x_.tolist()

# converting decimal to binary
for i in range(len(pix_secret)):
    for j in range(len(pix_secret)):
        pix_secret[i][j]=bin(pix_secret[i][j]).replace("0b", "")

# converting to 8-bit pixels 
temp3=[]
temp3+=h.conversion_8bit(pix_secret)

# getting the psnr of stego image
print(d.return_psnr(pix,temp3))
